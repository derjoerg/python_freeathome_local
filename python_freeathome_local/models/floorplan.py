"""Asynchronous Python client for Free@Home."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
import textwrap
from .floor import Floor

@dataclass
class Floorplan:
    """Model for a Floorplan."""

    __floors: {}

    def __init__(self, config: dict[str, Any]):
        self.__floors = {}

        for key, value in config.items():
            floorId = int(key, 16)
            floor = Floor(floorId, value)

            self.__floors[floorId] = floor

    def __str__(self) -> str:
        string = (
            f"Floors: {len(self.__floors)}"
        )

        for key, floor in self.__floors.items():
            value = str(floor)
            string = (
                f"{string}\n"
                f"{textwrap.indent(value, '    ')}\n"
                f"----------"
            )

        return string

    def getFloorById(self, id: hex) -> Floor:
        return self.__floors[id]
