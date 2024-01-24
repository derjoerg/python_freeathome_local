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
class WindowDoorSensorChannel(AbstractChannel):
    """Model for a Window-Door-Sensor-Channel."""

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
        """Initialize a WindowDoorSensorChannel."""
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

    def getWindowDoor(self):
        """Return WindowDoor."""
        datapoint = self.getOutputByPairingID(PairingIDs.AL_WINDOW_DOOR)
        return datapoint.getValue() == "1"

    def getState(self):
        """Return WindowDoor."""
        return self.getWindowDoor()
