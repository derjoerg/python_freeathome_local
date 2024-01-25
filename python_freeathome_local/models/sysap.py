"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

import textwrap
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Self
from uuid import UUID

from .abstractdevice import AbstractDevice
from .devicefactory import DeviceFactory
from .floorplan import Floorplan

if TYPE_CHECKING:
    from ..exceptions import FreeAtHomeError
    from ..freeathome import FreeAtHome


@dataclass
class SysAp:
    """Model for a SysAp."""

    __api: FreeAtHome
    __id: UUID
    __connectionState: str
    __name: str
    __uartSerialNumber: str
    __version: str
    __devices: dict[str, AbstractDevice]
    __floorplan: Floorplan

    @classmethod
    def fromApi(
        cls,
        api: FreeAtHome,
        id: str,
        config: dict[str, Any],
        sysApOnly: bool = True,
    ) -> Self:
        """Initialize a SysAp device from the API."""
        try:
            correctId = UUID(str(id))
        except ValueError:
            msg = f"The provided id '{id}' is malformed."
            raise FreeAtHomeError(msg)

        if "connectionState" in config:
            connState = config["connectionState"]
        else:
            msg = "connectionState is not defined"
            raise FreeAtHomeError(msg)

        sysapName = ""

        if "sysapName" in config:
            sysapName = config["sysapName"]

        if "sysap" in config:
            uartSerialNumber = ""

            if "uartSerialNumber" in config["sysap"]:
                uartSerialNumber = config["sysap"]["uartSerialNumber"]

            version = ""

            if "version" in config["sysap"]:
                version = config["sysap"]["version"]

        else:
            msg = "SysapSection missing"
            raise FreeAtHomeError(msg)

        sysAp = cls(
            api=api,
            id=correctId,
            connectionState=connState,
            name=sysapName,
            uartSerialNumber=uartSerialNumber,
            version=version,
        )

        if sysApOnly is False:
            if "floorplan" in config:
                for key, value in config["floorplan"].items():
                    sysAp.__floorplan = Floorplan(value)

            if "devices" in config:
                for key, value in config["devices"].items():
                    device = DeviceFactory.create(sysAp, key, value)

                    if device is not None:
                        sysAp.setDevice(key, device)
        #                        sysAp.__devices[key] = device

        return sysAp

    def updateFromDict(self, data: dict[str, Any]) -> list:
        """Return list of updated datapoints from Free@Home API response.

        Args:
        ----
            data: Update everything based on the websocket data

        Returns:
        -------
            The updated datapoint objects as list.
        """
        datapoints = []

        if "datapoints" in data:
            for key, value in data["datapoints"].items():
                splitted = key.split("/", 1)
                # print(key, " has the value ", value)

                if splitted[0] in self.__devices:
                    datapoint = self.__devices[splitted[0]].updateFromDict(
                        splitted[1], value
                    )

                    if datapoint is not None:
                        datapoints.append(datapoint)
                        # print(
                        #     datapoint.getChannel().getDisplayName(),
                        #     " - ",
                        #     datapoint.getPairingID().name,
                        #     " : ",
                        #     datapoint.getValue()
                        # )

                # else:
                #    print(f"Not defined : {key} has the value {value}")

        return datapoints

    def __str__(self) -> str:
        """Redefine object-to-string."""
        string = (
            f"Name      : {self.__name}\n"
            f"Id        : {self.__id}\n"
            f"State     : {self.__connectionState}\n"
            f"uartSerial: {self.__uartSerialNumber}\n"
            f"Version   : {self.__version}\n"
            f"Devices   : {len(self.__devices)}"
        )

        for key, device in self.__devices.items():
            value = str(device)
            string = (
                f"{string}\n"
                f"{textwrap.indent(value, '    ')}\n"
                f"----------"
            )

        value = str(self.__floorplan)
        string = f"{string}\n" f"{textwrap.indent(value, '    ')}"

        return string

    def __init__(
        self,
        api: FreeAtHome,
        id: UUID,
        connectionState: str,
        name: str,
        uartSerialNumber: str,
        version: str,
    ) -> None:
        """Initialize a SysAp device class.

        Args:
        ----
            data: The full API response from a SysAp.

        Raises:
        ------
            FreeAtHomeError: In case the given API response is incomplete in a
                way that a Device object cannot be constructed from it.
        """
        self.__api = api
        self.__id = id
        self.__connectionState = connectionState
        self.__name = name
        self.__uartSerialNumber = uartSerialNumber
        self.__version = version
        self.__devices = {}

    def getApi(self) -> FreeAtHome:
        """Return API."""
        return self.__api

    def getId(self) -> UUID:
        """Return Id of SysAp."""
        return self.__id

    def getFloorplan(self) -> Floorplan:
        """Return Floorplan."""
        return self.__floorplan

    def getDeviceById(self, id: str) -> AbstractDevice:
        """Return specific Device by ID."""
        return self.__devices[id]

    def setDevice(self, key: str, device: AbstractDevice) -> None:
        """Set specific Device."""
        self.__devices[key] = device
