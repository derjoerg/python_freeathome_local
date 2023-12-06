"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .abstractdevice import AbstractDevice

@dataclass
class TPDevice(AbstractDevice):
    """Model for a TP-Device."""

    interface: str = "TP"

    def __init__(self, interface: str, serialNumber: str, floor: str, room: str, displayName: str, unresponsive: bool, unresponsiveCounter: int, defect: bool, channels: dict[str, Any]):
        super().__init__(
            serialNumber,
            floor,
            room,
            displayName,
            unresponsive,
            unresponsiveCounter,
            defect,
            channels
        )
        self.interface = interface
