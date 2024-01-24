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
class RainSensorChannel(AbstractChannel):
    """Model for a Rain-Sensor-Channel."""

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
        """Initialize a RainSensorChannel."""
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

    def getRainAlarm(self):
        """Return RainAlarm."""
        datapoint = self.getOutputByPairingID(PairingIDs.AL_RAIN_ALARM)
        return datapoint.getValue() == "1"

    def getState(self):
        """Return RainAlarm."""
        return self.getRainAlarm()

    def getRainSensorActivationPercentage(self):
        """Return RainSensorActivationPercentage."""
        datapoint = self.getOutputByPairingID(
            PairingIDs.AL_RAIN_SENSOR_ACTIVATION_PERCENTAGE
        )
        return float(datapoint.getValue())

    def getRainSensorFrequency(self):
        """Return RainSensorFrequency."""
        datapoint = self.getOutputByPairingID(
            PairingIDs.AL_RAIN_SENSOR_FREQUENCY
        )
        return float(datapoint.getValue())
