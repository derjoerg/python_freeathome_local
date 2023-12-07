"""Asynchronous Python client for Free@Home."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Room:
    """Model for a Room."""

    __id: hex = 0x0
    __name: str = ""

    def __init__(self, id: hex, config: dict[str, Any]):
        self.__id = id
        self.__name = ""

        if "name" in config:
            self.__name = config["name"]

    def __str__(self) -> str:
        return(
            f"{self.__id} - {self.__name}"
        )

    def getId(self) -> hex:
        return self.__id
    
    def getName(self) -> str:
        return self.__name
