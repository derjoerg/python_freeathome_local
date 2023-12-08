"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from .triggerchannel import TriggerChannel
from .temperaturesensorchannel import TemperatureSensorChannel
from .brightnesssensorchannel import BrightnessSensorChannel
from .switchactuatorchannel import SwitchActuatorChannel
from ..functionids import FunctionIDs
from .floor import Floor

@dataclass
class ChannelFactory:

    @classmethod
    def create(cls, device: AbstractDevice, identifier: str, config: dict[str, Any]) -> AbstractChannel:
        """Create a specific channel object based on provided config"""

        device = device
        floor = ""
        room = ""
        displayName = ""
        functionID = 0x0
        parameters = {}
        inputs = {}
        outputs = {}

        if "floor" in config:
            floor = config["floor"]

            if floor != "":
                floor = device.getSysAp().getFloorplan().getFloorById(int(floor, 16))
        
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

            if functionID == FunctionIDs.FID_TRIGGER.value:
                channel = TriggerChannel(device=device, identifier=identifier, floor=floor, room=room, displayName=displayName, functionID=FunctionIDs.FID_TRIGGER, parameters=parameters, inputs=inputs, outputs=outputs)
            elif functionID == FunctionIDs.FID_TEMPERATURE_SENSOR.value:
                channel = TemperatureSensorChannel(device=device, identifier=identifier, floor=floor, room=room, displayName=displayName, functionID=FunctionIDs.FID_TEMPERATURE_SENSOR, parameters=parameters, inputs=inputs, outputs=outputs)
            elif functionID == FunctionIDs.FID_BRIGHTNESS_SENSOR.value:
                channel = BrightnessSensorChannel(device=device, identifier=identifier, floor=floor, room=room, displayName=displayName, functionID=FunctionIDs.FID_TEMPERATURE_SENSOR, parameters=parameters, inputs=inputs, outputs=outputs)
            elif functionID == FunctionIDs.FID_SWITCH_ACTUATOR.value:
                channel = SwitchActuatorChannel(device=device, identifier=identifier, floor=floor, room=room, displayName=displayName, functionID=FunctionIDs.FID_SWITCH_ACTUATOR, parameters=parameters, inputs=inputs, outputs=outputs)

        try: channel
        except NameError: channel = None

        return channel
