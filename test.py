#!/usr/bin/python3
"""Testscript for the local Busch-Jaeger Free@Home API."""

import asyncio
import os

from dotenv import load_dotenv

from python_freeathome_local.freeathome import FreeAtHome


async def main() -> None:
    """Main function is called."""
    async with FreeAtHome(
        host=host,  # pylint: disable=used-before-assignment
        user=user,  # pylint: disable=used-before-assignment
        password=password,  # pylint: disable=used-before-assignment
    ) as freeathome:
        await freeathome.connect()
        sys_ap = await freeathome.load_sys_ap(False)

        if freeathome.connected:
            print("connected")
            # sys_ap
            print(sys_ap)
            # Weatherstation
            # print(
            #    sys_ap
            #    .get_device_by_identifier("7EB1000021C5")
            # )
            # BrightnessSensor
            # print(
            #    sys_ap
            #    .get_device_by_identifier("7EB1000021C5")
            #    .get_channel_by_identifier("ch0000")
            #    .get_state()
            # )
            # print(
            #    sys_ap
            #    .get_device_by_identifier("7EB1000021C5")
            #    .get_channel_by_identifier("ch0000")
            #    .get_brightness_alarm()
            # )
            # TemperatureSensor
            # print(
            #    sys_ap
            #    .get_device_by_identifier("7EB1000021C5")
            #    .get_channel_by_identifier("ch0002")
            #    .get_state()
            # )
            # print(
            #    sys_ap
            #    .get_device_by_identifier("7EB1000021C5")
            #    .get_channel_by_identifier("ch0002")
            #    .get_frost_alarm()
            # )
            # WindSensor
            # print(
            #    sys_ap
            #    .get_device_by_identifier("7EB1000021C5")
            #    .get_channel_by_identifier("ch0003")
            #    .get_state()
            # )
            # print(
            #    sys_ap
            #    .get_device_by_identifier("7EB1000021C5")
            #    .get_channel_by_identifier("ch0003")
            #    .get_wind_alarm()
            # )
            # print(
            #    sys_ap
            #    .get_device_by_identifier("7EB1000021C5")
            #    .get_channel_by_identifier("ch0003")
            #    .get_wind_force()
            # )
            # RainSensor
            # print(
            #    sys_ap
            #    .get_device_by_identifier("7EB1000021C5")
            #    .get_channel_by_identifier("ch0001")
            #    .get_state()
            # )
            # print(
            #    sys_ap
            #    .get_device_by_identifier("7EB1000021C5")
            #    .get_channel_by_identifier("ch0001")
            #    .get_rain_sensor_activation_percentage()
            # )
            # print(
            #    sys_ap
            #    .get_device_by_identifier("7EB1000021C5")
            #    .get_channel_by_identifier("ch0001")
            #    .get_rain_sensor_frequency()
            # )
            # WindowDoorSensor
            # print(
            #    sys_ap
            #    .get_device_by_identifier("ABB28CBC3651")
            #    .get_channel_by_identifier("ch0002")
            #    .get_state()
            # )
            # MovementDetector
            # print(
            #    sys_ap
            #    .get_device_by_identifier("ABB700DA100B")
            #    .get_channel_by_identifier("ch0000")
            # )
            # print(
            #    sys_ap
            #    .get_device_by_identifier("ABB700DA100B")
            #    .get_channel_by_identifier("ch0000")
            #    .get_brightness_level()
            # )
            # print(
            #    sys_ap
            #    .get_device_by_identifier("ABB700DA100B")
            #    .get_channel_by_identifier("ch0000")
            #    .get_state()
            # )
            # SwitchSensor
            # print(
            #    sys_ap
            #    .get_device_by_identifier("ABB700D9C0A4")
            #    .get_channel_by_identifier("ch0000")
            # )
            # print(
            #    sys_ap
            #    .get_device_by_identifier("ABB700D9C0A4")
            #    .get_channel_by_identifier("ch0000")
            #    .get_state()
            # )
            # ForceOnOffSensor
            # print(
            #     sys_ap
            #     .get_device_by_identifier("ABB700D9AD95")
            #     .get_channel_by_identifier("ch0000")
            # )
            # print(
            #     sys_ap
            #     .get_device_by_identifier("ABB700D9AD95")
            #     .get_channel_by_identifier("ch0000")
            #     .get_state()
            # )
            # BlindSensor
            # print(
            #     sys_ap
            #     .get_device_by_identifier("ABB700DAD681")
            #     .get_channel_by_identifier("ch0003")
            # )
            # print(
            #     sys_ap
            #     .get_device_by_identifier("ABB700DAD681")
            #     .get_channel_by_identifier("ch0003")
            #     .get_state()
            # )

            # Trigger
            # result = (
            #     await sys_ap
            #     .get_device_by_identifier("ABB28EBC3651")
            #     .get_channel_by_identifier("ch0012")
            #     .press()
            # )
            # SwitchActuator
            # result = (
            #     await sys_ap.get_device_by_identifier("ABB242AD3651")
            #     .get_channel_by_identifier("ch0003")
            #     .turn_on()
            # )
            # result = (
            #     await sys_ap.get_device_by_identifier("ABB242AD3651")
            #     .get_channel_by_identifier("ch0003")
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
                    "(",
                    datapoint.get_identifier(),
                    ")",
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
