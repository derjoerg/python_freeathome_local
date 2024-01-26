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

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        device: AbstractDevice,
        identifier: str,
        floor: Floor,
        room: Room,
        display_name: str,
        function_id: FunctionIDs,
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
            display_name,
            function_id,
            parameters,
            inputs,
            outputs,
        )

    def __str__(self) -> str:
        """Redefine object-to-string."""
        parent = super().__str__()
        return f"Trigger-Channel:\n" f"{parent}"

    def get_brightness_level(self) -> float:
        """Return BrightnessLevel."""
        datapoint = self.get_output_by_pairing_id(
            PairingIDs.AL_BRIGHTNESS_LEVEL
        )
        return float(datapoint.get_value())

    def get_state(self) -> float:
        """Return BrightnessLevel."""
        return self.get_brightness_level()

    def get_brightness_alarm(self) -> bool:
        """Return BrightnessAlarm."""
        datapoint = self.get_output_by_pairing_id(
            PairingIDs.AL_BRIGHTNESS_ALARM
        )
        return datapoint.get_value() == "1"
