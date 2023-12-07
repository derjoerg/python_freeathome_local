"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .abstractdatapoint import AbstractDatapoint

@dataclass
class OutputDatapoint(AbstractDatapoint):
    """Model for an Output-Datapoint."""

    def __init__(self, channel: AbstractChannel, identifier: str, pairingID: PairingIDs, value: str):
        super().__init__(
            channel,
            identifier,
            pairingID,
            value
        )

    def __str__(self) -> str:
        parent = super().__str__()
        return (
            f"Output-Datapoint:\n"
            f"{parent}"
        )
