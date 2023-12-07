"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
#from .sysap import SysAp
from .floor import Floor
from .tpdevice import TPDevice

@dataclass
class DeviceFactory:

    @classmethod
    def create(cls, sysAp: SysAp, serialNumber: str, config: dict[str, Any]) -> AbstractDevice:
        """Create a specific device object based on provided config"""

        floor = ""
        room = ""
        displayName = ""
        unresponsive = False
        unresponsiveCounter = 0
        defect = False
        channels = {}
        parameters = {}

        if "floor" in config:
            floor = config["floor"]

            if floor != "":
                floor = sysAp.getFloorplan().getFloorById(int(floor, 16))
        
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
        
        if "unresponsive" in config:
            unresponsive = config["unresponsive"]
        
        if "unresponsiveCounter" in config:
            unresponsiveCounter = config["unresponsiveCounter"]
        
        if "defect" in config:
            defect = config["defect"]
        
        if "channels" in config:
            channels = config["channels"]
        
        if "parameters" in config:
            parameters = config["parameters"]
        
        if "interface" in config:
            interface = config["interface"]

            if "sonos" == config["interface"]:
                """We ignore sonos devices"""
                print(f"We ignore the device '{serialNumber}' as it is a Sonos")
            elif "hue" == config["interface"]:
                """We ignore hue devices"""
                print(f"We ignore device '{serialNumber}' as it is a Hue")
            elif "TP" == config["interface"]:
                """TP devices will be processed"""
                print(f"Let's process device '{serialNumber}' as it is a TP device")
                device = TPDevice(
                    sysAp= sysAp,
                    interface= interface,
                    serialNumber= serialNumber,
                    floor= floor,
                    room= room,
                    displayName= displayName,
                    unresponsive= unresponsive,
                    unresponsiveCounter= unresponsiveCounter,
                    defect= defect,
                    channels= channels,
                    parameters= parameters
                )

                if len(device.getChannels()) == 0:
                    device = None

            else:
                """All other interface devices will be ignored"""
                print(f"We ignore device '{serialNumber}' with the interface '{interface}'")
        else:
            """We ignore devices without an interface"""
            print(f"The device '{serialNumber}' will be ignored")
        
        try: device
        except NameError: device = None

        return device
