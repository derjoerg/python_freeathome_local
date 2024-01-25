"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, Any

from ..pairingids import PairingIDs

if TYPE_CHECKING:
    from .abstractchannel import AbstractChannel


class AbstractDatapoint(ABC):
    """Model for an abstract Datapoint."""

    __channel: AbstractChannel
    __identifier: str = ""
    __pairingID: PairingIDs
    __value: str = ""

    def __init__(
        self,
        channel: AbstractChannel,
        identifier: str,
        pairingID: PairingIDs,
        value: str,
    ):
        """Initialize an AbstractDatapoint."""
        self.__channel = channel
        self.__identifier = identifier
        self.__pairingID = pairingID
        self.__value = value

    def __str__(self) -> str:
        """Redefine object-to-string."""
        string = (
            f"Identifier: {self.__identifier}\n"
            f"Pairing   : {self.__pairingID}\n"
            f"Value     : {self.__value}"
        )

        return string

    def getChannel(self) -> AbstractChannel:
        """Return Channel of the Datapoint."""
        return self.__channel

    def getIdentifier(self) -> str:
        """Return Identifier of the Datapoint."""
        return self.__identifier

    def getPairingID(self) -> PairingIDs:
        """Return PairingID of the Datapoint."""
        return self.__pairingID

    def setValue(self, value: Any) -> AbstractDatapoint:
        """Set value of the Datapoint."""
        if isinstance(value, bool):
            if value is True:
                value = 1
            elif value is False:
                value = 0

        self.__value = value
        return self

    def getValue(self) -> str:
        """Return value of the Datapoint."""
        return self.__value
