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
class TemperatureSensorChannel(AbstractChannel):
    """Model for a Temperature-Sensor-Channel."""

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
        """Initialize TemperatureSensorChannel."""
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

    def getOutdoorTemperature(self):
        """Return OutdoorTemperature."""
        datapoint = self.getOutputByPairingID(PairingIDs.AL_OUTDOOR_TEMPERATURE)
        return float(datapoint.getValue())

    def getState(self):
        """Return OutdoorTemperature."""
        return self.getOutdoorTemperature()

    def getFrostAlarm(self):
        """Return FrostAlarm."""
        datapoint = self.getOutputByPairingID(PairingIDs.AL_FROST_ALARM)
        return datapoint.getValue() == "1"
