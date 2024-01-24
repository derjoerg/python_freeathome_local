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
class WindSensorChannel(AbstractChannel):
    """Model for a Wind-Sensor-Channel."""

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
        """Initialize a WindowSensorChannel."""
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

    def getWindSpeed(self):
        """Return WindSpeed."""
        datapoint = self.getOutputByPairingID(PairingIDs.AL_WIND_SPEED)
        return float(datapoint.getValue())

    def getState(self):
        """Return WindSpeed."""
        return self.getWindSpeed()

    def getWindAlarm(self):
        """Return WindAlarm."""
        datapoint = self.getOutputByPairingID(PairingIDs.AL_WIND_ALARM)
        return datapoint.getValue() == "1"

    def getWindForce(self):
        """Return WindForce."""
        datapoint = self.getOutputByPairingID(PairingIDs.AL_WIND_FORCE)
        return int(datapoint.getValue())
