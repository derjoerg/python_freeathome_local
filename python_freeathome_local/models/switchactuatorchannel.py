"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from ..pairingids import PairingIDs
from .abstractchannel import AbstractChannel

if TYPE_CHECKING:
    from ..functionids import FunctionIDs
    from .abstractdevice import AbstractDevice
    from .floor import Floor
    from .room import Room


@dataclass
class SwitchActuatorChannel(AbstractChannel):
    """Model for a SwitchActuator-Channel."""

    def __init__(
        self,
        device: AbstractDevice,
        identifier: str,
        floor: Floor,
        room: Room,
        displayName: str,
        functionID: FunctionIDs,
        parameters: dict[str, Any],
        inputs: dict[str, Any],
        outputs: dict[str, Any],
    ):
        """Initialize a SwitchActuatorChannel."""
        super().__init__(
            device,
            identifier,
            floor,
            room,
            displayName,
            functionID,
            parameters,
            inputs,
            outputs,
        )

    def __str__(self) -> str:
        """Redefine object-to-string."""
        parent = super().__str__()
        return f"Trigger-Channel:\n" f"{parent}"

    async def setSwitchOnOff(self, status: bool):  # type: ignore
        """Turn the channel on or off."""
        datapoint = self.getInputByPairingID(PairingIDs.AL_SWITCH_ON_OFF)
        return await datapoint.setValue(status)  # type: ignore

    async def turnOn(self):  # type: ignore
        """Turn on the channel."""
        return await self.setSwitchOnOff(True)

    async def turnOff(self):  # type: ignore
        """Turn off the channel."""
        return await self.setSwitchOnOff(False)

    async def setForced(self, status: bool):  # type: ignore
        """Set Forced."""
        datapoint = self.getInputByPairingID(PairingIDs.AL_FORCED)
        return await datapoint.setValue(status)  # type: ignore

    async def setTimedStartStop(self, status: bool):  # type: ignore
        """Set TimedStartStop."""
        datapoint = self.getInputByPairingID(PairingIDs.AL_TIMED_START_STOP)
        return await datapoint.setValue(status)  # type: ignore

    async def setTimedMovement(self, status: bool):  # type: ignore
        """Set TimedMovement."""
        datapoint = self.getInputByPairingID(PairingIDs.AL_TIMED_MOVEMENT)
        return await datapoint.setValue(status)  # type: ignore

    def getInfoOnOff(self) -> bool:
        """Return InfoOnOff."""
        datapoint = self.getOutputByPairingID(PairingIDs.AL_INFO_ON_OFF)
        return datapoint.getValue() == "1"

    def getState(self) -> bool:
        """Return InfoOnOff."""
        return self.getInfoOnOff()

    def getInfoForce(self) -> bool:
        """Return InfoForce."""
        datapoint = self.getOutputByPairingID(PairingIDs.AL_INFO_FORCE)
        return datapoint.getValue() == "1"

    def getInfoError(self) -> bool:
        """Return InfoError."""
        datapoint = self.getOutputByPairingID(PairingIDs.AL_INFO_ERROR)
        return datapoint.getValue() == "1"
