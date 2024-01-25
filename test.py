#!/usr/bin/python3

import asyncio
import os

from dotenv import load_dotenv

from python_freeathome_local.freeathome import FreeAtHome


async def main() -> None:
    async with FreeAtHome(
        host=host,
        user=user,
        password=password,
    ) as freeathome:
        await freeathome.connect()
        sys_ap = await freeathome.load_sys_ap(False)

        if freeathome.connected:
            print("connected")
            # sys_ap
            print(sys_ap)
            # Weatherstation
            # print(
            #     sys_ap
            #         .get_device_by_id("7EB1000021C5")
            # )
            # BrightnessSensor
            # print(
            #     sys_ap
            #         .get_device_by_id("7EB1000021C5")
            #         .get_channel_by_id("ch0000")
            #         .get_state()
            # )
            # print(
            #     sys_ap
            #         .get_device_by_id("7EB1000021C5")
            #         .get_channel_by_id("ch0000")
            #         .get_brightness_alarm()
            # )
            # TemperatureSensor
            # print(
            #     sys_ap
            #         .get_device_by_id("7EB1000021C5")
            #         .get_channel_by_id("ch0002")
            #         .get_state()
            # )
            # print(
            #     sys_ap
            #         .get_device_by_id("7EB1000021C5")
            #         .get_channel_by_id("ch0002")
            #         .get_frost_alarm()
            # )
            # WindSensor
            # print(
            #      sys_ap
            #         .get_device_by_id("7EB1000021C5")
            #         .get_channel_by_id("ch0003")
            #         .get_state()
            # )
            # print(
            #     sys_ap
            #         .get_device_by_id("7EB1000021C5")
            #         .get_channel_by_id("ch0003")
            #         .get_wind_alarm()
            # )
            # print(
            #     sys_ap
            #         .get_device_by_id("7EB1000021C5")
            #         .get_channel_by_id("ch0003")
            #         .get_wind_force()
            # )
            # RainSensor
            # print(
            #     sys_ap
            #         .get_device_by_id("7EB1000021C5")
            #         .get_channel_by_id("ch0001")
            #         .get_state()
            # )
            # print(
            #     sys_ap
            #         .get_device_by_id("7EB1000021C5")
            #         .get_channel_by_id("ch0001")
            #         .get_rain_sensor_activation_percentage()
            # )
            # print(
            #     sys_ap
            #         .get_device_by_id("7EB1000021C5")
            #         .get_channel_by_id("ch0001")
            #         .get_rain_sensor_frequency()
            # )
            # WindowDoorSensor
            # print(
            #     sys_ap
            #         .get_device_by_id("ABB28CBC3651")
            #         .get_channel_by_id("ch0002")
            #         .get_state()
            # )
            # MovementDetector
            # print(
            #     sys_ap
            #         .get_device_by_id("ABB700DA100B")
            #         .get_channel_by_id("ch0000")
            # )
            # print(
            #     sys_ap
            #         .get_device_by_id("ABB700DA100B")
            #         .get_channel_by_id("ch0000")
            #         .get_brightness_level()
            # )
            # print(
            #     sys_ap
            #         .get_device_by_id("ABB700DA100B")
            #         .get_channel_by_id("ch0000")
            #         .get_state()
            # )
            # SwitchSensor
            # print(
            #     sys_ap
            #         .get_device_by_id("ABB700D9C0A4")
            #         .get_channel_by_id("ch0000")
            # )
            # print(
            #     sys_ap
            #         .get_device_by_id("ABB700D9C0A4")
            #         .get_channel_by_id("ch0000")
            #         .get_state()
            # )

            # Trigger
            # result = await sys_ap
            #     .get_device_by_id("ABB28EBC3651")
            #     .get_channel_by_id("ch0012")
            # .press()
            # SwitchActuator
            # result = (
            #     await sys_ap.get_device_by_id("ABB242AD3651")
            #     .get_channel_by_id("ch0003")
            #     .turn_on()
            # )
            # result = (
            #     await sys_ap.get_device_by_id("ABB242AD3651")
            #     .get_channel_by_id("ch0003")
            #     .turn_off()
            # )

        def something_updated(datapoints) -> None:
            """Call when sys_ap reports a change."""
            print("\tReceived an update from sys_ap")

            for datapoint in datapoints:
                print(
                    datapoint.get_channel().get_device().get_serial_number(),
                    "(",
                    datapoint.get_channel().get_device().get_display_name(),
                    ")",
                    " - ",
                    datapoint.get_channel().get_identifier(),
                    "(",
                    datapoint.get_channel().get_display_name(),
                    ")",
                    " - ",
                    datapoint.get_pairing_id().name,
                    " : ",
                    datapoint.get_value(),
                )

        # Start listening
        task = asyncio.create_task(
            freeathome.listen(callback=something_updated)
        )

        # Now we stream for 10 seconds
        await asyncio.sleep(10)
        task.cancel()


if __name__ == "__main__":
    load_dotenv()

    host = os.getenv("HOST")
    user = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    asyncio.run(main())
