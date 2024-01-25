"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

import textwrap
from abc import ABC
from typing import TYPE_CHECKING, Any

from .abstractparameter import AbstractParameter
from .channelfactory import ChannelFactory
from .floor import Floor
from .parameterfactory import ParameterFactory
from .room import Room

if TYPE_CHECKING:
    from .abstractchannel import AbstractChannel
    from .abstractdatapoint import AbstractDatapoint
    from .sysap import SysAp


class AbstractDevice(ABC):
    """Model for an abstract Device."""

    __sysAp: SysAp
    __serialNumber: str = ""
    __floor: Floor | None = None
    __room: Room | None = None
    __displayName: str = ""
    __unresponsive: bool = False
    __unresponsiveCounter: int = 0
    __defect: bool = False
    __channels: dict[str, AbstractChannel]
    __parameters: dict[str, AbstractParameter]

    def __init__(
        self,
        sysAp: SysAp,
        serialNumber: str,
        floor: Floor | None,
        room: Room | None,
        displayName: str,
        unresponsive: bool,
        unresponsiveCounter: int,
        defect: bool,
        channels: dict[str, Any],
        parameters: dict[str, Any],
    ):
        """Initialize an AbstractDevice."""
        self.__sysAp = sysAp
        self.__serialNumber = serialNumber
        self.__floor = floor
        self.__room = room
        self.__displayName = displayName
        self.__unresponsive = unresponsive
        self.__unresponsiveCounter = unresponsiveCounter
        self.__defect = defect
        self.__channels = {}
        self.__parameters = {}

        for key, value in channels.items():
            channel = ChannelFactory.create(self, key, value)

            if channel is not None:
                self.__channels[key] = channel

        for key, value in parameters.items():
            parameter = ParameterFactory.create(key, value)

            if parameter is not None:
                self.__parameters[key] = parameter

    def __str__(self) -> str:
        """Redefine object-to-string."""
        string = (
            f"Serial  : {self.__serialNumber}\n"
            f"Name    : {self.__displayName}\n"
            f"Floor   : {self.__floor}\n"
            f"Room    : {self.__room}\n"
            f"Channels: {len(self.__channels)}"
        )

        for key, channel in self.__channels.items():
            value = str(channel)
            string = f"{string}\n" f"{textwrap.indent(value, '    ')}\n"

        string = (
            f"{string}\n"
            f"Parameters: {len(self.__parameters)}\n"
            f"----------"
        )

        for key, parameter in self.__parameters.items():
            value = str(parameter)
            string = f"{string}\n" f"{textwrap.indent(value, '    ')}\n"

        return string

    def getSysAp(self) -> SysAp:
        """Return SysAp of the Device."""
        return self.__sysAp

    def getSerialNumber(self) -> str:
        """Return SerialNumber of the Device."""
        return self.__serialNumber

    def getChannels(self) -> dict:
        """Return all Channels of the Device."""
        return self.__channels

    def getChannelById(self, id: str) -> AbstractChannel:
        """Return specific Channel of the Device."""
        return self.__channels[id]

    def getDisplayName(self) -> str:
        """Return DisplayName of the Device."""
        return self.__displayName

    def updateFromDict(self, key: str, value: str) -> AbstractDatapoint | None:
        """Return Channel object from Free@Home API response.

        Args:
        ----
            data: Update everything based on the websocket data

        Returns:
        -------
            The updated Datapoint object.
        """
        datapoint = None
        splitted = key.split("/")

        if splitted[0] in self.__channels:
            datapoint = self.__channels[splitted[0]].updateFromDict(
                splitted[1], value
            )

        return datapoint
