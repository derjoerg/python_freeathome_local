"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from abc import ABC, abstractmethod
import textwrap

from ..pairingids import PairingIDs

class AbstractDatapoint(ABC):
    """Model for an abstract Datapoint."""

    __channel: AbstractChannel | None = None
    __identifier: str = ""
    __pairingID: PairingIDs
    __value: str = ""

    def __init__(self, channel: AbstractChannel, identifier: str, pairingID: PairingIDs, value: str):
        self.__channel = channel
        self.__identifier = identifier
        self.__pairingID = pairingID
        self.__value = value

    def __str__(self) -> str:
        string = (
            f"Identifier: {self.__identifier}\n"
            f"Pairing   : {self.__pairingID}\n"
            f"Value     : {self.__value}"
        )

        return string

    def getChannel(self):
        return self.__channel

    def getIdentifier(self) -> str:
        return self.__identifier

    def getPairingID(self):
        return self.__pairingID

    def setValue(self, value):

        if type(value) == bool:

            if value == True:
                value = 1
            elif value == False:
                value = 0

        self.__value = value
        return self

    def getValue(self) -> str:
        return self.__value
