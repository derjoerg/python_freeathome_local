"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import UUID
import textwrap
from .abstractdevice import AbstractDevice
from .devicefactory import DeviceFactory
from .floorplan import Floorplan

@dataclass
class SysAp:
    """Model for a SysAp."""

    __id: UUID
    __connectionState: str
    __name: str
    __devices: {}
    __floorplan: Floorplan | None = None

    @classmethod
    def fromApi(cls, id: str, config: dict[str, Any], sysApOnly: bool = True) -> Self:
        """Initialize a SysAp device from the API.

        Args:
        ----
        """
        try:
            correctId = UUID(str(id))
        except ValueError:
            msg = f"The provided id '{id}' is malformed."
            raise FreeAtHomeError(msg)
        
        if "connectionState" in config:
            connState = config["connectionState"]
        else:
            msg = f"connectionState is not defined"
            raise FreeAtHomeError(msg)
        
        sysapName = ""

        if "sysapName" in config:
            sysapName = config["sysapName"]
        
        sysAp = cls(
            id= correctId,
            connectionState= connState,
            name= sysapName,
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

    def updateFromDict(self, data: dict[str, Any]) -> SysAp:
        """Return SysAp object from Free@Home API response.

        Args:
        ----
            data: Update everything based on the websocket data
        
        Returns:
        -------
            The updated SysAp object.
        """
        if "datapoints" in data:

            for key, value in data["datapoints"].items():
                print(key, " has the value ", value)

        return self

    def __str__(self) -> str:
        string = (
            f"Name   : {self.__name}\n"
            f"Id     : {self.__id}\n"
            f"State  : {self.__connectionState}\n"
            f"Devices: {len(self.__devices)}"
        )

        for key, device in self.__devices.items():
            value = str(device)
            string = (
                f"{string}\n"
                f"{textwrap.indent(value, '    ')}\n"
                f"----------"
            )

        value = str(self.__floorplan)
        string = (
            f"{string}\n"
            f"{textwrap.indent(value, '    ')}"
        )
        
        return string

    def __init__(self, id: str, connectionState: bool, name: str) -> None:
        """Initialize a SysAp device class.

        Args:
        ----
            data: The full API response from a SysAp.

        Raises:
        ------
            FreeAtHomeError: In case the given API response is incomplete in a
                way that a Device object cannot be constructed from it.
        """
        self.__id = id
        self.__connectionState = connectionState
        self.__name = name
        self.__devices = {}

    def getId(self) -> UUID:
        return self.__id

    def getFloorplan(self) -> Floorplan:
        return self.__floorplan

    def setDevice(self, key: str, device: AbstractDevice) -> None:
        self.__devices[key] = device
