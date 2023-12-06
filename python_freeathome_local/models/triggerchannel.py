"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .abstractchannel import AbstractChannel

@dataclass
class TriggerChannel(AbstractChannel):
    """Model for a Trigger-Channel."""

    def __init__(self, identifier: str, floor: str, room: str, displayName: str, functionId: FunctionIds):
        super().__init__(
            identifier,
            floor,
            room,
            displayName,
            functionId
        )
