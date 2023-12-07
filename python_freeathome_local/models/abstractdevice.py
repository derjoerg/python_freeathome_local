"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import textwrap

from .floor import Floor
from .room import Room
from .channelfactory import ChannelFactory
from .parameterfactory import ParameterFactory

class AbstractDevice(ABC):
    """Model for an abstract Device."""

    __sysAp: SysAp | None = None
    __serialNumber: str = ""
    __floor: Floor | None = None
    __room: Room | None = None
    __displayName: str = ""
    __unresponsive: bool = False
    __unresponsiveCounter: int = 0
    __defect: bool = False
    __channels: {}
    __parameters: {}

    def __init__(self, sysAp: SysAp, serialNumber: str, floor: Floor | None, room: Room | None, displayName: str, unresponsive: bool, unresponsiveCounter: int, defect: bool, channels: dict[str, Any], parameters: dict[str, Any]):
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
        string = (
            f"Serial  : {self.__serialNumber}\n"
            f"Name    : {self.__displayName}\n"
            f"Floor   : {self.__floor}\n"
            f"Room    : {self.__room}\n"
            f"Channels: {len(self.__channels)}"
        )

        for key, channel in self.__channels.items():
            value = str(channel)
            string = (
                f"{string}\n"
                f"{textwrap.indent(value, '    ')}\n"
            )
            
        string = (
            f"{string}\n"
            f"Parameters: {len(self.__parameters)}\n"
            f"----------"
        )

        for key, parameter in self.__parameters.items():
            value = str(parameter)
            string = (
                f"{string}\n"
                f"{textwrap.indent(value, '    ')}\n"
            )
        
        return string

    def getSysAp(self) -> SysAp:
        return self.__sysAp

    def getChannels(self) -> dict:
        return self.__channels
