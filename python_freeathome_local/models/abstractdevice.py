"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from .abstractchannel import AbstractChannel
from .channelfactory import ChannelFactory

class AbstractDevice(ABC):
    """Model for an abstract Device."""

    serialNumber: str = ""
    floor: str = ""
    room: str = ""
    displayName: str = ""
    unresponsive: bool = False
    unresponsiveCounter: int = 0
    defect: bool = False
    #channels: dict[str, AbstractChannel] | None = field(default_factory=dict)
    channels: {}

    def __init__(self, serialNumber: str, floor: str, room: str, displayName: str, unresponsive: bool, unresponsiveCounter: int, defect: bool, channels: dict[str, Any]):
        self.serialNumber = serialNumber
        self.floor = floor
        self.room = room
        self.displayName = displayName
        self.unresponsive = unresponsive
        self.unresponsiveCounter = unresponsiveCounter
        self.defect = defect
        self.channels = {}

        for key, value in channels.items():
            channel = ChannelFactory.create(key, value)

            if channel is not None:
                self.channels[key] = channel
