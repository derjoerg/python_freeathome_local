"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .abstractchannel import AbstractChannel
from ..pairingids import PairingIDs

@dataclass
class BrightnessSensorChannel(AbstractChannel):
    """Model for a Brightness-Sensor-Channel."""

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

    def getBrightnessLevel(self):
        datapoint = self.getOutputByPairingID(PairingIDs.AL_BRIGHTNESS_LEVEL)
        return float(datapoint.getValue())

    def getState(self):
        return self.getBrightnessLevel()

    def getBrightnessAlarm(self):
        datapoint = self.getOutputByPairingID(PairingIDs.AL_BRIGHTNESS_ALARM)
        return datapoint.getValue() == '1'
