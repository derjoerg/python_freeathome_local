"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from abc import ABC, abstractmethod

from ..functionids import FunctionIds

class AbstractChannel(ABC):
    """Model for an abstract Channel."""

    identifier: str = ""
    floor: str = ""
    room: str = ""
    displayName: str = ""
    functionId: FunctionIds

    def __init__(self, identifier: str, floor: str, room: str, displayName: str, functionId: FunctionIds):
        self.identifier = identifier
        self.floor = floor
        self.room = room
        self.displayName = displayName
        self.functionId = functionId
