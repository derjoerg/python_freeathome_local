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
        sysAp = await freeathome.getConfiguration(False)

        if freeathome.connected:
            print("connected")
            print(sysAp)
        
        def somethingUpdated(sysAp: SysAp) -> None:
            """Call when SysAp reports a change."""
            print("Received an update from SysAp")
            print(sysAp.connectionState)
        
        # Start listening
        task = asyncio.create_task(freeathome.listen(callback=somethingUpdated))

        # Now we stream for 30 seconds
        await asyncio.sleep(30)
        task.cancel()

if __name__ == "__main__":
    load_dotenv()

    host = os.getenv("HOST")
    user = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    asyncio.run(main())
