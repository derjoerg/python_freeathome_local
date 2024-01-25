"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from ..parameterids import ParameterIDs
from .parameter import Parameter

if TYPE_CHECKING:
    from .abstractparameter import AbstractParameter


@dataclass
class ParameterFactory:
    """Factory class for a Parameter."""

    @classmethod
    def create(cls, identifier: str, value: str) -> AbstractParameter:
        """Create a specific parameter object based on provided config."""
        parameterID = int(identifier[3:], 16)

        for param in ParameterIDs:
            if parameterID == param.value:
                break

        parameter = Parameter(
            identifier=identifier, parameterID=param, value=value
        )

        return parameter
