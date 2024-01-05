"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .abstractchannel import AbstractChannel
from ..pairingids import PairingIDs

@dataclass
class SwitchSensorChannel(AbstractChannel):
    """Model for a SwitchSensor-Channel."""

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

    #async def press(self):
    #    """Trigger the channel"""
    #
    #    for key, datapoint in self.getInputs().items():
    #
    #        if datapoint.getPairingID() == PairingIDs.AL_TIMED_START_STOP:
    #            return await datapoint.setValue(1)
