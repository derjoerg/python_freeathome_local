"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .abstractchannel import AbstractChannel
from ..pairingids import PairingIDs

@dataclass
class MovementDetectorChannel(AbstractChannel):
    """Model for a Movement-Detector-Channel."""

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

    def getInfoOnOff(self):
        """This will be only set if the movement detector is e.g. attached to a switch or light"""
        datapoint = self.getInputByPairingID(PairingIDs.AL_INFO_ON_OFF)
        return datapoint.getValue() == '1'

    def getState(self):
        return self.getInfoOnOff()

    def getBrightnessLevel(self):
        datapoint = self.getOutputByPairingID(PairingIDs.AL_BRIGHTNESS_LEVEL)
        return float(datapoint.getValue())

    def getTimedMovement(self):
        """This is a momentary switch, which is triggered if movement is detected"""
        """It is always true, just when it is triggered it is movement"""
        datapoint = self.getOutputByPairingID(PairingIDs.AL_TIMED_MOVEMENT)
        return datapoint.getValue() == '1'

    def getTimedPresence(self):
        """I don't know"""
        datapoint = self.getOutputByPairingID(PairingIDs.AL_TIMED_PRESENCE)
        return datapoint.getValue() == '1'
