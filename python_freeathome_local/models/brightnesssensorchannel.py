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
class BrightnessSensorChannel(AbstractChannel):
    """Model for a Brightness-Sensor-Channel."""

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
        """Initialize a BrightnessSensorChannel."""
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

    def getBrightnessLevel(self):
        """Return BrightnessLevel."""
        datapoint = self.getOutputByPairingID(PairingIDs.AL_BRIGHTNESS_LEVEL)
        return float(datapoint.getValue())

    def getState(self):
        """Return BrightnessLevel."""
        return self.getBrightnessLevel()

    def getBrightnessAlarm(self):
        """Return BrightnessAlarm."""
        datapoint = self.getOutputByPairingID(PairingIDs.AL_BRIGHTNESS_ALARM)
        return datapoint.getValue() == "1"
