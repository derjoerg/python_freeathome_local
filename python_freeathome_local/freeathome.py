"""Asynchronous Python client for the local Busch-Jaeger Free@Home API."""

from __future__ import annotations

import asyncio
import json
import socket
from base64 import b64encode
from collections.abc import Callable
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, cast

import aiohttp
from aiohttp import ClientSession, ClientWebSocketResponse
from aiohttp.hdrs import METH_GET, METH_PUT
from yarl import URL

from .exceptions import (
    FreeAtHomeConnectionClosedError,
    FreeAtHomeConnectionError,
    FreeAtHomeConnectionTimeoutError,
    FreeAtHomeEmptyResponseError,
    FreeAtHomeError,
)
from .models.inputdatapoint import InputDatapoint
from .models.sysap import SysAp

if TYPE_CHECKING:
    from type_extensions import Self


@dataclass
class FreeAtHome:
    """Main class for handling connections with Free@Home."""

    session: ClientSession | None = None
    requestTimeout: float = 10.0
    _client: ClientWebSocketResponse | None = None
    host: str = ""
    user: str = ""
    password: str = ""
    restPath: str = "/fhapi/v1/api/rest"
    wsPath: str = "/fhapi/v1/api/ws"
    _sysAp: SysAp | None = None
    _closeSession: bool = False

    @property
    def connected(self) -> bool:
        """Returns if we are connected to the WebSocket of a SysAp.

        Returns
        -------
            True if we are connected to the WebSocket of a SysAp,
            False otherwise.
        """
        return self._client is not None and not self._client.closed

    async def connect(self) -> None:
        """Connect to the WebSocket of a SysAp.

        Raises
        ------
            FreeAtHomeError: There is a generic problem with the WebSocket
                communication.
            FreeAtHomeConnectionError: Error occured while communicating with
                the SysAp via the WebSßcket
        """
        if self.connected:
            return

        if self.session is None:
            self.session = ClientSession()
            self._closeSession = True

        if not self.session:
            msg = "There is a generic problem with the session to the SysAp"
            raise FreeAtHomeError(msg)

        basicAuth = b64encode(
            (self.user + ":" + self.password).encode()
        ).decode("ascii")
        headers = {
            "Authorization": f"Basic {basicAuth}",
        }
        url = URL.build(scheme="ws", host=self.host, port=80, path=self.wsPath)

        try:
            self._client = await self.session.ws_connect(
                url=url, headers=headers
            )
        except (
            aiohttp.WSServerHandshakeError,
            aiohttp.ClientConnectionError,
            socket.gaierror,
        ) as excpetion:
            msg = (
                "Error occured while communicating with SysAp"
                f" on WebSocket at {self.host}"
            )
            raise FreeAtHomeConnectionError(msg) from excpetion

    async def listen(self, callback: Callable[[list], None]) -> None:
        """Listen for events on the FreeAtHome WebSocket.

        Args:
        ----
            callback: Method to call when a state update is receivecd from
                the SysAp.

        Raises:
        ------
            FreeAtHomeError: Not connected to a WebSocket.
            FreeAtHomeConnectionError: An connection error occured while
                connected to the SysAp.
            FreeAtHomeconnectionClosedError: The WebSocket connection to the
                SysAp has been closed.
        """
        if not self._client or not self.connected:
            msg = "Not connected a SysAp WebSocket"
            raise FreeAtHomeError(msg)

        while not self._client.closed:
            message = await self._client.receive()

            if message.type == aiohttp.WSMsgType.ERROR:
                raise FreeAtHomeConnectionError(self._client.exception())

            if message.type == aiohttp.WSMsgType.TEXT:
                messageData = message.json()

                if str(self._sysAp.getId()) == list(messageData.keys())[0]:
                    datapoints = self._sysAp.updateFromDict(
                        data=messageData[str(self._sysAp.getId())]
                    )
                    callback(datapoints)

            if message.type in (
                aiohttp.WSMsgType.CLOSE,
                aiohttp.WSMsgType.CLOSED,
                aiohttp.WSMsgType.CLOSING,
            ):
                msg = (
                    f"Connection to the SysAp WebSocket on "
                    f"{self.host} has been closed"
                )
                raise FreeAtHomeConnectionClosedError(msg)

    async def disconnect(self) -> None:
        """Disconnect from the WebSocket of a SysAp."""
        if not self._client or not self.connected:
            return

        await self._client.close()

    async def setDatapoint(self, datapoint: InputDatapoint):
        """Send value to a datapoint on the SysAp."""
        uri = (
            "datapoint/"
            + str(datapoint.getChannel().getDevice().getSysAp().getId())
            + "/"
            + datapoint.getChannel().getDevice().getSerialNumber()
            + "."
            + datapoint.getChannel().getIdentifier()
            + "."
            + datapoint.getIdentifier()
        )
        print(f"{uri}")
        data = str(datapoint.getValue())
        response = await self.request(uri=uri, method=METH_PUT, data=data)
        print(f"{response}")

    async def request(
        self,
        uri: str,
        method: str = METH_GET,
        data: dict[str, Any] | None = None,
    ) -> Any:
        """Handle a REST-request to Free@Home.

        A generic method for sending/handling HTTP requests done against
        the SysAp.

        Args:
        ----
            uri: Request URI, for example `/fhapi/v1`.
            method: HTTP method to use for the request e.g. "GET" or "POST"
            data: Dictionary of data to send to the SysAp.

        Return:
        ------
            A Python dictionary (JSON decoded) with the response from the
            SysAp.

        Raises:
            FreeAtHomeConnectionError: An error occured while communicating
                with the SysAp.
            FreeAtHomeConnectionTimeoutError: A timeout occured while
                communicating with the SysAp.
            FreeAtHomeError: Received an unexpected response from the SysAp.
        """
        url = URL.build(
            scheme="http",
            user=self.user,
            password=self.password,
            host=self.host,
            port=80,
            path=self.restPath,
        ).joinpath(uri)

        headers = {
            "User-Agent": "PythonFreeAtHome",
            "Accept": "application/json, text/plain, */*",
        }

        try:
            async with asyncio.timeout(self.requestTimeout):
                response = await self.session.request(
                    method,
                    url,
                    headers=headers,
                    data=data,
                )
            contentType = response.headers.get("Content-Type", "")

            if response.status // 100 in [4, 5]:
                contents = await response.read()
                response.close()

                if contentType == "application/json":
                    raise FreeAtHomeError(
                        response.status,
                        json.loads(contents.decode("utf8")),
                    )
                raise FreeAtHomeError(
                    response.status,
                    {"message": contents.decode("utf8")},
                )

            if "application/json" in contentType:
                responseData = await response.json()
            else:
                responseData = await response.text()

        except TimeoutError as exception:
            msg = f"Timeout occured while connecting to SysAp at {self.host}"
            raise FreeAtHomeConnectionTimeoutError(msg) from exception
        except (aiohttp.ClientError, socket.gaierror) as exception:
            msg = f"Error occured while communicating with SysAp at {self.host}"
            raise FreeAtHomeConnectionError(msg) from exception

        return cast(dict[str, Any], responseData)

    async def loadSysAp(self, sysApOnly: bool = True) -> SysAp:
        """Get all configuration from the SysAp in a single call.

        This method receives all SysAp information available with a single
        API call.

        Returns:
        -------
            SysAp

        Raises:
        ------
            FreeAtHomeEmptyResponseError: The SysAp returned an empty response.
        """
        #        if self._sysAp is None:
        response = await self.request("configuration", METH_GET)

        if 1 == len(response):
            uuid = list(response.keys())[0]
            self._sysAp = SysAp.fromApi(self, uuid, response[uuid], sysApOnly)

        if self._sysAp is None:
            msg = f"The needed configuration was not received from {self.host}"
            raise FreeAtHomeEmptyResponseError(msg) from Exception

        return self._sysAp

    async def close(self) -> None:
        """Close open client (WebSocket) session."""
        await self.disconnect()

        if self.session and self._closeSession:
            await self.session.close()

    async def __aenter__(self) -> Self:
        """Async enter.

        Returns
        -------
            The FreeAtHome object.
        """
        return self

    async def __aexit__(self, *_exc_info: object) -> None:
        """Async exit.

        Args:
        ----
            _exc_info: Exec type.
        """
        await self.close()
