"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from ..functionids import FunctionIDs
from .brightnesssensorchannel import BrightnessSensorChannel  # noqa: F401
from .floor import Floor
from .movementdetectorchannel import MovementDetectorChannel  # noqa: F401
from .rainsensorchannel import RainSensorChannel  # noqa: F401
from .switchactuatorchannel import SwitchActuatorChannel  # noqa: F401
from .switchsensorchannel import SwitchSensorChannel  # noqa: F401
from .temperaturesensorchannel import TemperatureSensorChannel  # noqa: F401
from .triggerchannel import TriggerChannel  # noqa: F401
from .windowdoorsensorchannel import WindowDoorSensorChannel  # noqa: F401
from .windsensorchannel import WindSensorChannel  # noqa: F401

if TYPE_CHECKING:
    from .abstractchannel import AbstractChannel
    from .abstractdevice import AbstractDevice


@dataclass
class ChannelFactory:
    """Factory class for a channel."""

    @classmethod
    def create(
        cls, device: AbstractDevice, identifier: str, config: dict[str, Any]
    ) -> AbstractChannel:
        """Create a specific channel object based on provided config."""
        device = device
        floor = ""
        room = ""
        displayName = ""
        functionID = 0x0
        parameters = {}
        inputs = {}
        outputs = {}
        channel = None

        if "floor" in config:
            floor = config["floor"]

            if floor != "":
                floor = (
                    device.getSysAp()
                    .getFloorplan()
                    .getFloorById(int(floor, 16))
                )

        if floor == "":
            floor = None

        if "room" in config:
            room = config["room"]

            if room != "" and isinstance(floor, Floor):
                room = floor.getRoomById(int(room, 16))

        if room == "":
            room = None

        if "displayName" in config:
            displayName = config["displayName"]

        if "parameters" in config:
            parameters = config["parameters"]

        if "inputs" in config:
            inputs = config["inputs"]

        if "outputs" in config:
            outputs = config["outputs"]

        if "functionID" in config and config["functionID"] != "":
            functionID = int(config["functionID"], 16)
            print(f"\t{functionID} - {FunctionIDs(functionID).name}")

            if functionID in FunctionIDs:
                className = (
                    FunctionIDs(functionID)
                    .name.removeprefix("FID_")
                    .title()
                    .replace("_", "")
                    + "Channel"
                )

                try:
                    channel = globals()[className](
                        device=device,
                        identifier=identifier,
                        floor=floor,
                        room=room,
                        displayName=displayName,
                        functionID=FunctionIDs(functionID),
                        parameters=parameters,
                        inputs=inputs,
                        outputs=outputs,
                    )
                    print("\t\tok")
                except KeyError:
                    # channel = None
                    print(f"\t\t{className} not defined")

        return channel
