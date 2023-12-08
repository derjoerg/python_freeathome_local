"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .abstractchannel import AbstractChannel

@dataclass
class TemperatureSensorChannel(AbstractChannel):
    """Model for a Temperature-Sensor-Channel."""

    def __init__(self, device: AbstractDevice, identifier: str, floor: Floor, room: Room, displayName: str, functionID: FunctionIDs, parameters: dict[str, Any], inputs: dict[str, Any], outputs: dict[str, Any]):
        super().__init__(
            device,
            identifier,
            floor,
            room,
            displayName,
            functionID,
            parameters,
            inputs,
            outputs
        )

    def __str__(self) -> str:
        parent = super().__str__()
        return (
            f"Trigger-Channel:\n"
            f"{parent}"
        )
