"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .inputdatapoint import InputDatapoint
from .outputdatapoint import OutputDatapoint
from ..pairingids import PairingIDs

@dataclass
class DatapointFactory:

    @classmethod
    def create(cls, channel:AbstractDatapoint, identifier: str, config: dict[str, Any]) -> AbstractDatapoint:
        """Create a specific parameter object based on provided config"""

        pairingID = ""
        value = ""

        if "value" in config:
            value = config["value"]

        if "pairingID" in config:
            #pairingID = int(config["pairingID"],16)
            pairingID = config["pairingID"]

        for pairing in PairingIDs:

            if pairingID == pairing.value:
                break

        if "i" == identifier[:1]:
            datapoint = InputDatapoint(channel=channel, identifier=identifier, pairingID=pairing, value=value)
        elif "o" == identifier[:1]:
            datapoint = OutputDatapoint(channel=channel, identifier=identifier, pairingID=pairing, value=value)

        try: datapoint
        except NameError: datapoint = None

        return datapoint
