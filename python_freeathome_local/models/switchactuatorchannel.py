"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .abstractchannel import AbstractChannel
from ..pairingids import PairingIDs

@dataclass
class SwitchActuatorChannel(AbstractChannel):
    """Model for a SwitchActuator-Channel."""

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

    async def setSwitchOnOff(self, status: bool):
        """Turns the channel on or off"""
        datapoint = self.getInputByPairingID(PairingIDs.AL_SWITCH_ON_OFF)
        return await datapoint.setValue(status)

    async def turnOn(self):
        """Turns the channel on"""
        return await self.setSwitchOnOff(True)

    async def turnOff(self):
        """Turns the channel off"""
        return await self.setSwitchOnOff(False)

    async def setForced(self, status: bool):
        datapoint = self.getInputByPairingID(PairingIDs.AL_FORCED)
        return await datapoint.setValue(status)

    async def setTimedStartStop(self, status: bool):
        datapoint = self.getInputByPairingID(PairingIDs.AL_TIMED_START_STOP)
        return await datapoint.setValue(status)

    async def setTimedMovement(self, status: bool):
        datapoint = self.getInputByPairingID(PairingIDs.AL_TIMED_MOVEMENT)
        return await datapoint.setValue(status)

    def getInfoOnOff(self):
        datapoint = self.getOutputByPairingID(PairingIDs.AL_INFO_ON_OFF)
        return datapoint.getValue() == '1'

    def getState(self):
        return self.getInfoOnOff()

    def getInfoForce(self):
        datapoint = self.getOutputByPairingID(PairingIDs.AL_INFO_FORCE)
        return datapoint.getValue() == '1'

    def getInfoError(self):
        datapoint = self.getOutputByPairingID(PairingIDs.AL_INFO_ERROR)
        return datapoint.getValue() == '1'
