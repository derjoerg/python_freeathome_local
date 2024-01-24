"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

import textwrap
from dataclasses import dataclass
from typing import Any

from .room import Room


@dataclass
class Floor:
    """Model for a Floor."""

    __id: hex = 0x0
    __name: str = ""
    __rooms: {} | None = None

    def __init__(self, id: hex, config: dict[str, Any]):
        """Initialize a Floor."""
        self.__id = id
        self.__name = ""
        self.__rooms = {}

        if "name" in config:
            self.__name = config["name"]

        if "rooms" in config:
            for key, value in config["rooms"].items():
                roomId = int(key, 16)
                room = Room(roomId, value)

                self.__rooms[roomId] = room

    def __str__(self) -> str:
        """Redefine object-to-string."""
        string = f"{self.__id} - {self.__name}\n" f"Rooms: {len(self.__rooms)}"

        for key, room in self.__rooms.items():
            value = str(room)
            string = (
                f"{string}\n"
                f"{textwrap.indent(value, '    ')}\n"
                f"----------"
            )

        return string

    def getRoomById(self, id: hex) -> Room:
        """Return Room by specific ID."""
        return self.__rooms[id]

    def getId(self) -> hex:
        """Return Id of a Floor."""
        return self.__id

    def getName(self) -> str:
        """Return Name of a Floor."""
        return self.__name
