"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .triggerchannel import TriggerChannel
from ..functionids import FunctionIds

@dataclass
class ChannelFactory:

    @classmethod
    def create(cls, identifier: str, config: dict[str, Any]) -> AbstractChannel:
        """Create a specific channel object based on provided config"""

        floor = ""
        room = ""
        displayName = ""
        functionId = 0x0

        if "floor" in config:
            floor = config["floor"]
        
        if "room" in config:
            room = config["room"]
        
        if "displayName" in config:
            displayName = config["displayName"]
        
        if "functionID" in config and config["functionID"] != "":
            functionId = int(config["functionID"], 16)

            if functionId == FunctionIds.FID_TRIGGER.value:
                channel = TriggerChannel(identifier=identifier, floor=floor, room=room, displayName=displayName, functionId=FunctionIds.FID_TRIGGER)

        try: channel
        except NameError: channel = None

        return channel
