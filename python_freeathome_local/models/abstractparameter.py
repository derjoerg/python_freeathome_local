"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from abc import ABC

from ..parameterids import ParameterIDs


class AbstractParameter(ABC):
    """Model for an abstract Parameter."""

    __identifier: str = ""
    __parameterID: ParameterIDs
    __value: str = ""

    def __init__(self, identifier: str, parameterID: ParameterIDs, value: str):
        """Initialize an AbstractParameter."""
        self.__identifier = identifier
        self.__parameterID = parameterID
        self.__value = value

    def __str__(self) -> str:
        """Redefine object-to-string."""
        return f"{self.__identifier} - {self.__value} - {self.__parameterID}"
