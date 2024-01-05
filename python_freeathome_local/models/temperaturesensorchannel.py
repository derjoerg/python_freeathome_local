"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .abstractchannel import AbstractChannel
from ..pairingids import PairingIDs

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

    def getOutdoorTemperature(self):
        datapoint = self.getOutputByPairingID(PairingIDs.AL_OUTDOOR_TEMPERATURE)
        return float(datapoint.getValue())

    def getState(self):
        return self.getOutdoorTemperature()

    def getFrostAlarm(self):
        datapoint = self.getOutputByPairingID(PairingIDs.AL_FROST_ALARM)
        return datapoint.getValue() == '1'
