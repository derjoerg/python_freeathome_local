"""Asynchronous Python client for Free@Home."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from .floor import Floor
from .tpdevice import TPDevice

if TYPE_CHECKING:
    from .abstractdevice import AbstractDevice
    from .sysap import SysAp


@dataclass
class DeviceFactory:
    """Factory class for a device."""

    @classmethod
    def create(
        cls, sysAp: SysAp, serialNumber: str, config: dict[str, Any]
    ) -> AbstractDevice | None:
        """Create a specific device object based on provided config."""
        origFloor = ""
        origRoom = ""
        displayName = ""
        unresponsive = False
        unresponsiveCounter = 0
        defect = False
        channels = {}
        parameters = {}
        returnOK = False

        if "floor" in config:
            origFloor = config["floor"]

            if origFloor != "":
                floor = sysAp.getFloorplan().getFloorById(int(origFloor, 16))

        if "room" in config:
            origRoom = config["room"]

            if origRoom != "" and isinstance(floor, Floor):
                room = floor.getRoomById(int(origRoom, 16))

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
                print(
                    f"Let's process device '{serialNumber}' "
                    f"with the name '{displayName}' as it is a TP device"
                )
                device = TPDevice(
                    sysAp=sysAp,
                    interface=interface,
                    serialNumber=serialNumber,
                    floor=floor if "floor" in locals() else None,
                    room=room if "room" in locals() else None,
                    displayName=displayName,
                    unresponsive=unresponsive,
                    unresponsiveCounter=unresponsiveCounter,
                    defect=defect,
                    channels=channels,
                    parameters=parameters,
                )
                returnOK = True

                if len(device.getChannels()) == 0:
                    returnOK = False
                    print("\tNo channels, so not added.")

            else:
                """All other interface devices will be ignored"""
                print(
                    f"We ignore device '{serialNumber}' "
                    f"with the interface '{interface}' "
                    f"and the name '{displayName}'"
                )
        else:
            """We ignore devices without an interface"""
            print(
                f"The device '{serialNumber}' "
                f"with the name '{displayName}' will be ignored"
            )

        return device if returnOK is True else None
