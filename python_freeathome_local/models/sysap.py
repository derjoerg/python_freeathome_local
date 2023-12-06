"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import UUID
from .abstractdevice import AbstractDevice
from .devicefactory import DeviceFactory

@dataclass
class SysAp:
    """Model for a SysAp."""

    id: UUID
    connectionState: str
    name: str
    devices: dict[str, AbstractDevice] | None = field(default_factory=dict)

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

            if "devices" in config:

                for key, value in config["devices"].items():
                    device = DeviceFactory.create(key, value)

                    if device is not None:
                        sysAp.devices[key] = device

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

#    def __init__(self, data: dict[str, Any] | None) -> None:
#        """Initialize a SysAp device class.
#
#        Args:
#        ----
#            data: The full API response from a SysAp.
#
#        Raises:
#        ------
#            FreeAtHomeError: In case the given API response is incomplete in a
#                way that a Device object cannot be constructed from it.
#        """
#        print(data)
