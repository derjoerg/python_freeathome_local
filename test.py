#!/usr/bin/python3

import asyncio
from dotenv import load_dotenv
import os

from python_freeathome_local.freeathome import FreeAtHome
from python_freeathome_local.models.sysap import SysAp
from python_freeathome_local.functionids import FunctionIDs

async def main() -> None:
    async with FreeAtHome(
        host=host,
        user=user,
        password=password,
    ) as freeathome:
        await freeathome.connect()
        sysAp = await freeathome.loadSysAp(False)

        if freeathome.connected:
            print("connected")
            # SysAp
            #print(sysAp)
            # Weatherstation
            #print(sysAp.getDeviceById("7EB1000021C5"))
            # BrightnessSensor
            #print(sysAp.getDeviceById("7EB1000021C5").getChannelById("ch0000").getState())
            #print(sysAp.getDeviceById("7EB1000021C5").getChannelById("ch0000").getBrightnessAlarm())
            # TemperatureSensor
            #print(sysAp.getDeviceById("7EB1000021C5").getChannelById("ch0002").getState())
            #print(sysAp.getDeviceById("7EB1000021C5").getChannelById("ch0002").getFrostAlarm())
            # WindSensor
            #print(sysAp.getDeviceById("7EB1000021C5").getChannelById("ch0003").getState())
            #print(sysAp.getDeviceById("7EB1000021C5").getChannelById("ch0003").getWindAlarm())
            #print(sysAp.getDeviceById("7EB1000021C5").getChannelById("ch0003").getWindForce())
            # RainSensor
            #print(sysAp.getDeviceById("7EB1000021C5").getChannelById("ch0001").getState())
            #print(sysAp.getDeviceById("7EB1000021C5").getChannelById("ch0001").getRainSensorActivationPercentage())
            #print(sysAp.getDeviceById("7EB1000021C5").getChannelById("ch0001").getRainSensorFrequency())
            # WindowDoorSensor
            #print(sysAp.getDeviceById("ABB28CBC3651").getChannelById("ch0002").getState())
            # MovementDetector
            #print(sysAp.getDeviceById("ABB700DA100B").getChannelById("ch0000"))
            #print(sysAp.getDeviceById("ABB700DA100B").getChannelById("ch0000").getBrightnessLevel())
            #print(sysAp.getDeviceById("ABB700DA100B").getChannelById("ch0000").getState())
            #SwitchSensor
            print(sysAp.getDeviceById("ABB700D9C0A4").getChannelById("ch0000"))
            print(sysAp.getDeviceById("ABB700D9C0A4").getChannelById("ch0000").getState())

            # Trigger
            #result = await sysAp.getDeviceById("ABB28EBC3651").getChannelById("ch0012").press()
            # SwitchActuator
            #result = await sysAp.getDeviceById("ABB242AD3651").getChannelById("ch0003").turnOn()
            #result = await sysAp.getDeviceById("ABB242AD3651").getChannelById("ch0003").turnOff()
        
        def somethingUpdated(datapoints) -> None:
            """Call when SysAp reports a change."""
            print("\tReceived an update from SysAp")

            for datapoint in datapoints:
                    print(
                        datapoint.getChannel().getDevice().getSerialNumber(),
                        '(', datapoint.getChannel().getDevice().getDisplayName(), ')',
                        ' - ',
                        datapoint.getChannel().getIdentifier(),
                        '(', datapoint.getChannel().getDisplayName(), ')',
                        ' - ',
                        datapoint.getPairingID().name, ' : ', datapoint.getValue()
                    )
        
        # Start listening
        task = asyncio.create_task(freeathome.listen(callback=somethingUpdated))

        # Now we stream for 10 seconds
        await asyncio.sleep(10)
        task.cancel()

if __name__ == "__main__":
    load_dotenv()

    host = os.getenv("HOST")
    user = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    asyncio.run(main())
