#!/usr/bin/python3

import asyncio
from dotenv import load_dotenv
import os

from python_freeathome_local.freeathome import FreeAtHome
from python_freeathome_local.models.sysap import SysAp

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
            #print(sysAp)
            #result = await sysAp.getDeviceById("ABB28EBC3651").getChannelById("ch0012").press()
            #result = await sysAp.getDeviceById("ABB242AD3651").getChannelById("ch0003").turnOn()
            #result = await sysAp.getDeviceById("ABB242AD3651").getChannelById("ch0003").turnOff()
        
        def somethingUpdated(sysAp: SysAp) -> None:
            """Call when SysAp reports a change."""
            print("Received an update from SysAp")
        
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
