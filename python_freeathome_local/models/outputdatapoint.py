"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .abstractdatapoint import AbstractDatapoint

if TYPE_CHECKING:
    from ..pairingids import PairingIDs
    from .abstractchannel import AbstractChannel


@dataclass
class OutputDatapoint(AbstractDatapoint):
    """Model for an Output-Datapoint."""

    def __init__(
        self,
        channel: AbstractChannel,
        identifier: str,
        pairingID: PairingIDs,
        value: str,
    ):
        """Initialize an OutputDatapoint."""
        super().__init__(channel, identifier, pairingID, value)

    def __str__(self) -> str:
        """Redefine object-to-string."""
        parent = super().__str__()
        return f"Output-Datapoint:\n" f"{parent}"
