"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .abstractparameter import AbstractParameter

@dataclass
class Parameter(AbstractParameter):
    """Model for a Parameter."""

    def __init__(self, identifier: str, parameterID: ParameterIDs, value: str):
        super().__init__(
            identifier,
            parameterID,
            value
        )
