"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .parameter import Parameter
from ..parameterids import ParameterIDs

@dataclass
class ParameterFactory:

    @classmethod
    def create(cls, identifier: str, value: str) -> AbstractParameter:
        """Create a specific parameter object based on provided config"""

        parameterID = int(identifier[3:],16)

        for param in ParameterIDs:

            if parameterID == param.value:
                break
        
        parameter = Parameter(identifier=identifier, parameterID=param, value=value)

        try: parameter
        except NameError: parameter = None

        return parameter
