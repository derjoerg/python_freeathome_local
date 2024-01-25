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
class SwitchSensorChannel(AbstractChannel):
    """Model for a SwitchSensor-Channel."""

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
        """Initialize a SwitchSensorChannel."""
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

    def get_switch_on_off(self) -> bool:
        """Return SwitchOnOff."""
        datapoint = self.get_output_by_pairing_id(PairingIDs.AL_SWITCH_ON_OFF)
        return datapoint.get_value() == "1"

    def get_state(self) -> bool:
        """Return SwitchOnOff."""
        return self.get_switch_on_off()
