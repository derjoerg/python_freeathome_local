"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .abstractdevice import AbstractDevice

@dataclass
class TPDevice(AbstractDevice):
    """Model for a TP-Device."""

    __interface: str = "TP"

    def __init__(self, sysAp: SysAp, interface: str, serialNumber: str, floor: Floor | None, room: Room | None, displayName: str, unresponsive: bool, unresponsiveCounter: int, defect: bool, channels: dict[str, Any], parameters: dict[str, Any]):
        super().__init__(
            sysAp,
            serialNumber,
            floor,
            room,
            displayName,
            unresponsive,
            unresponsiveCounter,
            defect,
            channels,
            parameters
        )
        self.__interface = interface

    def __str__(self) -> str:
        parent = super().__str__()
        return (
            f"TP-Device:\n"
            f"Interface: {self.__interface}\n"
            f"{parent}"
        )
