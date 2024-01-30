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
class DesDoorRingingSensorChannel(AbstractChannel):
    """Model for a DesDoorRingingSensor-Channel."""

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
        """Initialize a DesDoorRingingSensorChannel."""
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
        return f"DesDoorRinging-Channel:\n" f"{parent}"

    def get_timed_start_stop(self) -> bool:
        """Return Timed Start Stop."""
        datapoint = self.get_output_by_pairing_id(
            PairingIDs.AL_TIMED_START_STOP
        )
        return datapoint.get_value() == "1"

    def get_state(self) -> bool:
        """Return Timed Start Stop."""
        return self.get_timed_start_stop()
