"""Asynchronous Python client for the local Busch-Jaeger Free@Home API."""

from enum import Enum

# flake8: noqa: E501
# pylint: disable=line-too-long


class PairingIDs(Enum):
    """All PairingIDs from FreeAtHome."""

    AL_SWITCH_ON_OFF = 0x0001  # Binary Switch value
    AL_TIMED_START_STOP = 0x0002  # For staircase lighting or movement detection
    AL_FORCED = 0x0003  # Forces value dependent high priority on or off state
    AL_SCENE_CONTROL = (
        0x0004  # Recall or learn the set value related to encoded scene number
    )
    AL_TIMED_MOVEMENT = 0x0006  # Activation of an autonomous switch off function triggered by an movement detector
    AL_TIMED_PRESENCE = 0x0007  # Announces presence triggered by an movement detector to be used by e.g. RTCs. Is independent of brightness and can be used for alerts e.g.
    AL_RELATIVE_SET_VALUE_CONTROL = 0x0010  # Relative dimming value
    AL_ABSOLUTE_SET_VALUE_CONTROL = 0x0011  # Absolute control of the set value
    AL_NIGHT = (
        0x0012  # Toggle between day and night where day = 0 and night = 1
    )
    AL_RESET_ERROR = 0x0013  # Resets load failures / short circuits / etc
    AL_RGB = 0x0015  # RGB Color coded in three bytes
    AL_COLOR_TEMPERATURE = 0x0016  # Color temperature
    AL_HSV = 0x0017  # Hue (2 Byte) / Saturation (1 Byte) / Value (1 Byte / brightness)
    AL_COLOR = 0x0018  # Hue (2 Byte)
    AL_SATURATION = 0x0019  # Saturation (1 Byte)
    AL_ABSOLUTE_SET_VALUE_CONTROL_HUE = 0x001A  # Absolute control of the set value (does not switch on the light)
    AL_MOVE_UP_DOWN = 0x0020  # Moves sunblind up (0) and down (1)
    AL_STOP_STEP_UP_DOWN = 0x0021  # Stops the sunblind and to step it up/down
    AL_SET_ABSOLUTE_POSITION_BLINDS_PERCENTAGE = (
        0x0023  # Moves the sunblinds into a specified position
    )
    AL_SET_ABSOLUTE_POSITION_SLATS_PERCENTAGE = (
        0x0024  # Moves the slats into a specified position
    )
    AL_WIND_ALARM = 0x0025  # State of the wind sensor (sent cyclically and on COV) Moves the sunblind to a secure position and to block it for any further control
    AL_FROST_ALARM = 0x0026  # State of the frost sensor (sent cyclically and on COV) Moves the sunblind to a secure position and to block it for any further control
    AL_RAIN_ALARM = (
        0x0027  # State of the rain sensor (sent cyclically and on COV)
    )
    AL_FORCED_UP_DOWN = (
        0x0028  # Forces value dependent high priority up or down state
    )
    AL_WINDOW_DOOR_POSITION = (
        0x0029  # Delivers position for Window/Door (Open / Tilted / Closed)
    )
    AL_ACTUATING_VALUE_HEATING = (
        0x0030  # Determines the through flow volume of the control valve
    )
    AL_FAN_COIL_LEVEL = 0x0031  # Display value of  the fan coil speed. (0=off / 1=lowest - 5=fastest)
    AL_ACTUATING_VALUE_COOLING = (
        0x0032  # Determines the through flow volume of the control valve
    )
    AL_SET_POINT_TEMPERATURE = (
        0x0033  # Defines the displayed set point temperature of the system
    )
    AL_RELATIVE_SET_POINT_TEMPERATURE = (
        0x0034  # Defines the relative set point temperature of the system
    )
    AL_WINDOW_DOOR = 0x0035  # Open = 1 / closed = 0
    AL_STATE_INDICATION = (
        0x0036  # states: on/off heating/cooling; eco/comfort; frost/not frost
    )
    AL_FAN_MANUAL_ON_OFF = (
        0x0037  # Switches Fan in manual control mode (master to slave)
    )
    AL_CONTROLLER_ON_OFF = (
        0x0038  # Switches controller on or off. Off means protection mode
    )
    AL_RELATIVE_SET_POINT_REQUEST = (
        0x0039  # Request for a new relative set point value
    )
    AL_ECO_ON_OFF = 0x003A  # Switches eco mode on or off
    AL_COMFORT_TEMPERATURE = 0x003B  # Sends the current comfort temperature
    AL_ABSOLUTE_SET_VALUE_CONTROL_WHITE = (
        0x003C  # Absolute control of the white set value
    )
    AL_SELECTED_HEATING_COOLING_MODE_REQUEST = (
        0x003D  # Request a change in selected heating/cooling mode
    )
    AL_INFO_HEATING_COOLING_MODE = 0x003E  # Info heating/cooling mode
    AL_FAN_STAGE_REQUEST = 0x0040  # Request for a new manual fan stage
    AL_FAN_MANUAL_ON_OFF_REQUEST = (
        0x0041  # Request for switching fan in manual/auto mode
    )
    AL_CONTROLLER_ON_OFF_REQUEST = 0x0042  # Request for switching controller on or off. Off means protection mode
    AL_ECO_ON_OFF_INDICATION = 0x0044  # Indicates ECO mode
    AL_CONTROLLER_ON_OFF_REQUEST_EXT = 0x0045  # Request for switching controller on or off. Off means protection mode
    AL_ECO_ON_OFF_EXT = 0x0046  # Switches eco mode on or off
    AL_RELATIVE_SET_POINT_REQUEST_EXT = (
        0x0047  # Request for a new relative set point value
    )
    AL_AWAY = 0x0050  # Indicates auto mode
    AL_INFO_ON_OFF = 0x0100  # Reflects the binary state of the actuator
    AL_INFO_FORCE = (
        0x0101  # Indicates the cause of forced operation (0 = not forced)
    )
    AL_SYSAP_INFO_ON_OFF = (
        0x0105  # Reflects the binary state of the actuator group
    )
    AL_SYSAP_INFO_FORCE = 0x0106  # Indicates whether the actuator group is forced (1) or not forced (0)
    AL_INFO_ACTUAL_DIMMING_VALUE = (
        0x0110  # Reflects the actual value of the actuator
    )
    AL_INFO_ERROR = 0x0111  # Indicates load failures / short circuits / etc
    AL_SYSAP_INFO_ACTUAL_DIMMING_VALUE = (
        0x0115  # Reflects the actual value of the actuator group
    )
    AL_SYSAP_INFO_ERROR = (
        0x0116  # Indicates load failures / short circuits / etc
    )
    AL_INFO_RGB = 0x0117  # RGB Color coded in three bytes
    AL_INFO_COLOR_TEMPERATURE = 0x0118  # Color temperature
    AL_SYSAP_INFO_RGB = 0x0119  # RGB Color coded in three bytes
    AL_SYSAP_INFO_COLOR_TEMPERATURE = 0x011A  # Color temperature
    AL_INFO_HSV = (
        0x011B  # Hue (2 Byte) Saturation (1 Byte); Value (1 Byte - brightness)
    )
    AL_SYSAP_INFO_HSV = (
        0x011C  # Hue (2 Byte) Saturation (1 Byte); Value (1 Byte - brightness)
    )
    AL_INFO_COLOR_MODE = 0x011D  # hsv or ct
    AL_SYSAP_INFO_COLOR_MODE = 0x011E  # hsv or ct
    AL_COLOR_MODE = 0x011F  # hsv or ct
    AL_INFO_MOVE_UP_DOWN = 0x0120  # Indicates last moving direction and whether moving  currently or not
    AL_CURRENT_ABSOLUTE_POSITION_BLINDS_PERCENTAGE = (
        0x0121  # Indicate the current position of the sunblinds in percentage
    )
    AL_CURRENT_ABSOLUTE_POSITION_SLATS_PERCENTAGE = (
        0x0122  # Indicate the current position of the slats in percentage
    )
    AL_SYSAP_INFO_MOVE_UP_DOWN = 0x0125  # Indicates last moving direction and whether moving  currently or not of the actuator group
    AL_SYSAP_CURRENT_ABSOLUTE_POSITION_BLINDS_PERCENTAGE = 0x0126  # indicate the current position of the sunblinds in percentage of the actuator group
    AL_SYSAP_CURRENT_ABSOLUTE_POSITION_SLATS_PERCENTAGE = 0x0127  # indicate the current position of the slats in percentage of the actuator group
    AL_MEASURED_TEMPERATURE = (
        0x0130  # Indicates the actual measured temperature
    )
    AL_INFO_VALUE_HEATING = (
        0x0131  # States the current flow volume of the conrol valve
    )
    AL_INFO_VALUE_COOLING = (
        0x0132  # States the current flow volume of the conrol valve
    )
    AL_HEATING_COOLING = (
        0x0135  # switch between heating and cooling: heating = 0 / cooling = 1
    )
    AL_ACTUATING_FAN_STAGE_HEATING = (
        0x0136  # Requests a new manual fan stage from actuator in heating mode
    )
    AL_INFO_ABSOLUTE_SET_POINT_REQUEST = (
        0x0140  # Absolute set point temperature input for timer
    )
    AL_INFO_ACTUATING_VALUE_ADD_HEATING = 0x0141  # Feedback
    AL_INFO_ACTUATING_VALUE_ADD_COOLING = 0x0142  # Feedback
    AL_ACTUATING_VALUE_ADD_HEATING = 0x0143  #
    AL_ACTUATING_VALUE_ADD_COOLING = 0x0144  #
    AL_INFO_FAN_ACTUATING_STAGE_HEATING = 0x0145  # Feedback from FCA
    AL_INFO_FAN_MANUAL_ON_OFF_HEATING = 0x0146  # Feedback from FCA
    AL_ACTUATING_FAN_STAGE_COOLING = (
        0x0147  # Requests a new manual fan stage from actuator in cooling mode
    )
    AL_INFO_FAN_ACTUATING_STAGE_COOLING = (
        0x0149  # Feedback for current fan stage in cooling mode
    )
    AL_INFO_FAN_MANUAL_ON_OFF_COOLING = (
        0x014A  # Feedback for manual fan control cooling mode
    )
    AL_HEATING_ACTIVE = 0x014B  #
    AL_COOLING_ACTIVE = 0x014C  #
    AL_HEATING_DEMAND = 0x014D  #
    AL_COOLING_DEMAND = 0x014E  #
    AL_INFO_HEATING_DEMAND = 0x014F  #
    AL_INFO_COOLING_DEMAND = 0x0150  #
    AL_HUMIDITY = 0x0151  # Measured Humidity
    AL_AUX_ON_OFF_REQUEST = 0x0152  # Aux On/Off request
    AL_AUX_ON_OFF_RESPONSE = 0x0153  # Aux On/Off response
    AL_HEATING_ON_OFF_REQUEST = 0x0154  # Heating On/Off request
    AL_COOLING_ON_OFF_REQUEST = 0x0155  # Cooling On/Off request
    AL_OPERATION_MODE = 0x0156  #
    AL_SWING_MODE = 0x0157  #
    AL_SUPPORTED_FEATURES = 0x0158  #
    AL_EXTENDED_STATUS = 0x0159  #
    AL_EXTENDED_STATUS_US = 0x015A  #
    AL_AUX_HEATING_ON_OFF_REQUEST = 0x015B  #
    AL_EMERGENCY_HEATING_ON_OFF_REQUEST = 0x015C  #
    AL_OPERATION_MODE_32 = 0x015D  #
    AL_INFO_OPERATION_MODE_32 = 0x015E  #
    AL_INFO_SUPPORTED_OPERATION_MODE_32 = 0x015F  #
    AL_RELATIVE_FAN_SPEED_CONTROL = 0x0160  # Relative control of the set value
    AL_ABSOLUTE_FAN_SPEED_CONTROL = 0x0161  # Absolute control of the set value
    AL_INFO_ABSOLUTE_FAN_SPEED = (
        0x0162  # Reflects the actual value of the actuator
    )
    AL_SYSAP_INFO_ABSOLUTE_FAN_SPEED = (
        0x0163  # Reflects the actual value of the actuator
    )
    AL_TIMED_MOVEMENT_REQUEST = 0x0164  # Activation of an autonomous switch off function triggered by an movement detector
    AL_INFO_TIMED_MOVEMENT = 0x0165  # Reflects the actual value of the actuator
    AL_MOVEMENT_DETECTOR_STATUS = (
        0x0166  # Reflects the actual value of the actuator
    )
    AL_LOCK_SENSOR = 0x0167  # Locks a sensor for local on-site operation
    AL_INFO_LOCKED_SENSOR = 0x0168  # Reflects the locked state of a sensor
    AL_SYSAP_INFO_LOCKED_SENSOR = (
        0x0169  # Reflects the locked state of a sensor group
    )
    AL_INFO_SWING_MODE = 0x016A  #
    AL_INFO_SUPPORTED_SWING_MODE = 0x016B  #
    AL_INFO_VALUE_WHITE = 0x0170  # Feedback value white
    AL_SYSAP_INFO_VALUE_WHITE = 0x0171  # SysAP Feedback value white
    AL_NOTIFICATION_FLAGS = (
        0x01A0  # Notifications of RF devices (e. g. Battery low)
    )
    AL_INFO_LOCAL_TIMER_CONTROL_8 = 0x01A1  # local timer control for 8 timers
    AL_INFO_GROUP_TIMER_CONTROL_8 = 0x01A2  # group timer control for 8 timers
    AL_MWIRE_SWITCH_ON_OFF = 0x01A3  # Binary Switch value
    AL_MWIRE_RELATIVE_SET_VALUE_CONTROL = 0x01A4  # Relative dimming value
    AL_MWIRE_MOVE_UP_DOWN = 0x01A5  # Moves sunblind up (0) and down (1)
    AL_MWIRE_STOP_STEP_UP_DOWN = (
        0x01A6  # Stops the sunblind and to step it up/down
    )
    AL_MWIRE_PRESET = 0x01A7  # MWIRE preset number
    AL_INFO_LOCAL_TIMER_CONTROL_32 = 0x01A8  # local timer control for 32 timers
    AL_INFO_GROUP_TIMER_CONTROL_32 = 0x01A9  # group timer control for 32 timers
    AL_TRIGGERED_PIR_MASK = 0x01AA  #
    AL_TIMEFRAME_MOVEMENT = 0x01AB  # Activation of a delayed autonomous switch off function triggered by a movement detector over an extended time period
    AL_TIMED_DIMMING = 0x01AC  # Dim to a given value in a given time
    AL_INFO_TIMED_DIMMING = 0x01AD  # Target dimming feedback
    AL_BOOL_VALUE_1 = 0x0280  # Bool Value 1
    AL_BOOL_VALUE_2 = 0x0281  # Bool Value 2
    AL_BOOL_VALUE_3 = 0x0282  # Bool Value 3
    AL_SCALING_VALUE_1 = 0x0290  # Scaling Value 1
    AL_SCALING_VALUE_2 = 0x0291  # Scaling Value 2
    AL_SCALING_VALUE_3 = 0x0292  # Scaling Value 3
    AL_UNLOCK = 0x02A0  # Unlock command
    AL_LOCATOR_BEEP = 0x02C0  # Locator Beep
    AL_SWITCH_TEST_ALARM = 0x02C1  # Switch Test Alarm
    AL_TEST_ALARM_ACTIVE = 0x02C2  # Test-Alarm Active
    AL_FIRE_ALARM_ACTIVE = 0x02C3  # Fire-Alarm Active
    AL_CO_ALARM_ACTIVE = 0x02C4  # CO-Alarm Active
    AL_REMOTE_LOCATE = 0x02C5  # Remote locate
    AL_DETECTOR_PAIRING_MODE = 0x02C6  # Detector pairing mode
    AL_INFO_DETECTOR_PAIRING_MODE = 0x02C7  # Info detector pairing mode
    AL_FLOOD_ALARM = 0x02C8  # Flood detected
    AL_OUTDOOR_TEMPERATURE = 0x0400  # Outdoor Temperature
    AL_WIND_FORCE = 0x0401  # Wind force
    AL_BRIGHTNESS_ALARM = 0x0402  # Brightness alarm
    AL_BRIGHTNESS_LEVEL = 0x0403  # Weatherstation brightness level
    AL_WIND_SPEED = 0x0404  # Wind speed
    AL_RAIN_SENSOR_ACTIVATION_PERCENTAGE = 0x0405  #
    AL_RAIN_SENSOR_FREQUENCY = 0x0406  #
    AL_MEDIA_PLAY = 0x0440  # Start playing
    AL_MEDIA_PAUSE = 0x0441  # Pause/Stop playing
    AL_MEDIA_NEXT = 0x0442  # Play next title
    AL_MEDIA_PREVIOUS = 0x0443  # Play previous title
    AL_MEDIA_PLAY_MODE = 0x0444  # Play mode (shuffle / repeat)
    AL_MEDIA_MUTE = 0x0445  # Mute (1) and unmute (0) a player
    AL_RELATIVE_VOLUME_CONTROL = (
        0x0446  # Relative volume control. See also relative dimming
    )
    AL_ABSOLUTE_VOLUME_CONTROL = 0x0447  # Set player volume
    AL_GROUP_MEMBERSHIP = 0x0448  #
    AL_PLAY_FAVORITE = 0x0449  #
    AL_PLAY_NEXT_FAVORITE = 0x044A  #
    AL_PLAYBACK_STATUS = 0x0460  #
    AL_INFO_MEDIA_CURRENT_ITEM_METADATA = 0x0461  #
    AL_INFO_MUTE = 0x0462  #
    AL_INFO_ACTUAL_VOLUME = 0x0463  #
    AL_ALLOWED_PLAYBACK_ACTIONS = 0x0464  #
    AL_INFO_GROUP_MEMBERSHIP = 0x0465  #
    AL_INFO_PLAYING_FAVORITE = 0x0466  #
    AL_ABSOLUTE_GROUP_VOLUME_CONTROL = 0x0467  #
    AL_INFO_ABSOLUTE_GROUP_VOLUME = 0x0468  #
    AL_INFO_CURRENT_MEDIA_SOURCE = 0x0469  #
    AL_SOLAR_POWER_PRODUCTION = 0x04A0  # Power from the sun
    AL_INVERTER_OUTPUT_POWER = 0x04A1  # Output power of inverter (pbatt+Psun)
    AL_SOLAR_ENERGY_TODAY = 0x04A2  # Produced Energy
    AL_INJECTED_ENERGY_TODAY = 0x04A3  # Energy into the grid
    AL_PURCHASED_ENERGY_TODAY = 0x04A4  # Energy from the grid
    AL_NOTIFICATION_RUN_STANDALONE = (
        0x04A5  # Inverter is working in stand alone mode
    )
    AL_SELF_CONSUMPTION = 0x04A6  # production PV/ Total consumption
    AL_SELF_SUFFICIENCY = 0x04A7  # Consumption from PV/ Total consumption
    AL_HOME_POWER_CONSUMPTION = 0x04A8  # Power in home (PV and grid)
    AL_POWER_TO_GRID = 0x04A9  # Power from and to the grid: Purchased (less than 0), Injection (more than 0)
    AL_CONSUMED_ENERGY_TODAY = 0x04AA  # Energy bought from grid per day
    AL_NOTIFICATION_METER_COMMUNICATION_ERROR_WARNING = (
        0x04AB  # Meter communication loss
    )
    AL_SOC = 0x04AC  # Battery level
    AL_BATTERY_POWER = (
        0x04AD  # Batter power: Discharge (less then 0), Charge (more then 0)
    )
    AL_BOOST_ENABLE_REQUEST = (
        0x04B0  # 1: Boost enable request, 0: boost disable request
    )
    AL_SWITCH_CHARGING = 0x04B1  # 1: Enable charging session requested, 0: Stop charging session requested
    AL_STOP_ENABLE_CHARGING_REQUEST = 0x04B2  # 1: Enable charging when cable is plugged in, 0: Disable next charging session but charge until cable is plugged
    AL_INFO_BOOST = 0x04B3  # 1: Boost enabled, 0: boost disabled
    AL_INFO_WALLBOX_STATUS = 0x04B4  # Wallbox status 00000001: car plugged in, 00000002: Authorization granted, 00000004: Not charging, battery fully loaded, 40000000: charging stopped due to blackout prevention, 80000000: Ground fault error
    AL_INFO_CHARGING = 0x04B5  # 1: Charging, 0: Not charging
    AL_INFO_CHARGING_ENABLED = 0x04B6  # 1: Charging enabled for next session, 0: Charging disabled for next session
    AL_INFO_INSTALLED_POWER = 0x04B7  # Installed power (e.g. 20 kW)
    AL_INFO_ENERGY_TRANSMITTED = (
        0x04B8  # Energy transmitted so far per session (in Wh)
    )
    AL_INFO_CAR_RANGE = 0x04B9  # Car range in km per sessions
    AL_INFO_START_OF_CHARGING_SESSION = (
        0x04BA  # Start of charging session (in minutes in UTC)
    )
    AL_INFO_LIMIT_FOR_CHARGER = 0x04BB  # Limit for charger (in A)
    AL_INFO_ALBUM_COVER_URL = 0x04BD  # Album cover URL
    AL_INFO_CURRENT_SOLAR_POWER = 0x04BE  # Current Solar power
    AL_INFO_CURRENT_INVERTER_OUTPUT_POWER = (
        0x04BF  # Output power of inverter (pbatt+Psun)
    )
    AL_INFO_CURRENT_HOME_POWER_CONSUMPTION = (
        0x04C0  # Power in home (PV and grid)
    )
    AL_INFO_CURRENT_POWER_TO_GRID = 0x04C1  # Power from and to the grid: Purchased (less than 0), Injection (more than 0)
    AL_INFO_CURRENT_BATTERY_POWER = (
        0x04C2  # Batter power: Discharge (less then 0), Charge (more then 0)
    )
    AL_INFO_TOTAL_ENERGY_FROM_GRID = 0x04C3  # Total energy from grid
    AL_INFO_TOTAL_ENERGY_TO_GRID = 0x04C4  # Total energy to grid
    AL_MEASURED_CURRENT_POWER_CONSUMED = 0x04C5  # Current power consumed
    AL_MEASURED_IMPORTED_ENERGY_TODAY = 0x04C6  # Production and import of energy for today (grid purchase, battery discharge, PV production)
    AL_MEASURED_EXPORTED_ENERGY_TODAY = 0x04C7  # Consumption and export of energy for today (grid feed-in, battery charging, consumer consumption)
    AL_MEASURED_TOTAL_ENERGY_IMPORTED = 0x04C8  # Total production and import of energy (grid purchase, battery discharge, PV production)
    AL_MEASURED_TOTAL_ENERGY_EXPORTED = 0x04C9  # Total consumption and export of energy (grid feed-in, battery charging, consumer consumption)
    AL_SWITCH_ECO_CHARGING_ON_OFF = 0x04CA  #
    AL_INFO_ECO_CHARGING_ON_OFF = 0x04CB  #
    AL_LIMIT_FOR_CHARGER = 0x04CC  # Limit for charger (in A)
    AL_MEASURED_CURRENT_EXCESS_POWER = 0x04CD  # Current excess power
    AL_MEASURED_TOTAL_WATER = 0x04CE  # Measured total water consumption
    AL_MEASURED_TOTAL_GAS = 0x04CF  # Measured total gas consumption
    AL_CONSUMED_WATER_TODAY = 0x04D0  # Consumed water today
    AL_CONSUMED_GAS_TODAY = 0x04D1  # Consumed gas today
    AL_MEASURED_VOLTAGE = 0x04D2  # Measured voltage
    AL_MEASURED_CURRENT = 0x04D3  # Measured current
    AL_MIN_CHARGING_CURRENT_ECO = 0x04D4  # Minimum charging current in eco mode
    AL_INFO_MIN_CHARGING_CURRENT_ECO = (
        0x04D5  # Minimum charging current in eco mode
    )
    AL_USED_PHASES = 0x04D6  # Number of phases used for charging
    AL_INFO_USED_PHASES = 0x04D7  # Number of phases used for charging
    AL_FREE_VENDING = 0x04D8  # Allow free vending
    AL_INFO_FREE_VENDING = 0x04D9  # Allow free vending
    AL_INFO_MAXIMUM_CHARGING_CURRENT_LIMIT = (
        0x04DA  # Maximum limit for charger (in A)
    )
    AL_IMPORTED_ENERGY_COST_TODAY = 0x04DB  # Imported energy cost today
    AL_EXPORTED_ENERGY_COST_TODAY = 0x04DC  # Exported energy cost today
    AL_TOTAL_ENERGY_COST_IMPORTED = 0x04DD  # Total imported energy cost
    AL_TOTAL_ENERGY_COST_EXPORTED = 0x04DE  # Total exported energy cost
    AL_PAUSE_CHARGING = 0x04DF  # Pauses the charging
    AL_DISARM_SYSTEM = (
        0x0501  # Encrypted control datapoint for domus alarm center
    )
    AL_DISARM_COUNTER = (
        0x0502  # Info about the next counter to disarm the system
    )
    AL_INFO_INTRUSION_ALARM = 0x0504  # Intrusion Alarm
    AL_INFO_SAFETY_ALARM = 0x0505  # Safety Alarm
    AL_INFO_ERROR_STATUS = (
        0x0507  # Domus alarm device negative feedback and configuration info.
    )
    AL_ENABLE_CONFIGURATION = (
        0x0508  # Encrypted control datapoint for entering configuration mode
    )
    AL_DOMUS_ZONE_CONTROL = 0x0509  # Arm/Disarm a Zone
    AL_DOMUS_KEY_INFO = 0x050A  # Manufacturer ID +  Serial + AES Key
    AL_ZONE_STATUS = 0x050B  # Zone status
    AL_INFO_CONFIGURATION_STATUS = (
        0x050D  # Indicates configuration status and timewindow
    )
    AL_DOMUS_DISARM_DELAY_TIME = (
        0x050E  # Absolute number of seconds when the zone will be armed
    )
    AL_DOMUS_SIGNAL_STRENGTH = 0x05D8  # 2 Bit per Channel
    AL_START_STOP = 0x0600  # Starts / Stops operation
    AL_PAUSE_RESUME = 0x0601  #
    AL_SELECT_PROGRAM = 0x0602  #
    AL_DELAYED_START_TIME = 0x0603  #
    AL_INFO_STATUS = 0x0604  #
    AL_INFO_REMOTE_START_ENABLED = 0x0605  #
    AL_INFO_PROGRAM = 0x0606  #
    AL_INFO_FINISH_TIME = 0x0607  #
    AL_INFO_DELAYED_START_TIME = 0x0608  #
    AL_INFO_DOOR = 0x0609  #
    AL_INFO_DOOR_ALARM = 0x060A  #
    AL_SWITCH_SUPERCOOL = 0x060B  #
    AL_SWITCH_SUPERFREEZE = 0x060C  #
    AL_INFO_SWITCH_SUPERCOOL = 0x060D  #
    AL_INFO_SWITCH_SUPERFREEZE = 0x060E  #
    AL_CURRENT_TEMPERATURE_APPLIANCE_1 = 0x060F  #
    AL_CURRENT_TEMPERATURE_APPLIANCE_2 = 0x0610  #
    AL_SETPOINT_TEMPERATURE_APPLIANCE_1 = 0x0611  #
    AL_SETPOINT_TEMPERATURE_APPLIANCE_2 = 0x0612  #
    AL_CHANGE_OPERATION = 0x0613  #
    AL_INFO_VERBOSE_STATUS = 0x0614  #
    AL_INFO_REMAINING_TIME = (
        0x0615  # Remaining time till status change (start, finish, etc.)
    )
    AL_INFO_STATUS_CHANGED_TIME = (
        0x0616  # Time of last status change (start, finish, etc.)
    )
    AL_ACTIVE_ENERGY_V64 = 0x0617  # Active Energy (8 Byte)
    AL_LOCK_UNLOCK_COMMAND = 0x0618  # Lock/Unlock door command (1 Bit)
    AL_INFO_LOCK_UNLOCK_COMMAND = 0x0619  # Info Lock/Unlock door(1 Bit)
    AL_INFO_PRESSURE = 0x061A  # Measured air pressure
    AL_INFO_CO_2 = 0x061B  # Carbon dioxide level
    AL_INFO_CO = 0x061C  # Carbon monoxide level
    AL_INFO_NO_2 = 0x061D  # Nitrogen dioxide level
    AL_INFO_O_3 = 0x061E  # Ozone level
    AL_INFO_PM_10 = 0x061F  # PM10 level
    AL_INFO_PM_2_5 = 0x0620  # PM2.5 level
    AL_INFO_VOC = 0x0621  # VOC level
    AL_INFO_VOC_INDEX = 0x0622  # VOC level indexed
    AL_TRIGGER_CAMERA_CONFIG = 0x0623  # Open menu on panel
    AL_INFO_CAMERA_CONFIG = 0x0626  # Info config menu on Panel
    AL_INFO_CAMERA_ID = 0x0627  # Info camera id
    AL_CO2_ALERT = 0x0628  # CO2 alert
    AL_VOC_ALERT = 0x0629  # VOC alert
    AL_HUMIDITY_ALERT = 0x062A  # Humidity alert
    AL_AUTONOMOUS_SWITCH_OFF_TIME = 0x062B  #
    AL_INFO_AUTONOMOUS_SWITCH_OFF_TIME = 0x062C  #
    AL_INFO_PLAYLIST = 0x062D  #
    AL_INFO_AUDIO_INPUT = 0x062E  #
    AL_SELECT_PROFILE = 0x062F  #
    AL_INFO_RUNNING = 0x0630  # Feedback: Operation is running
    AL_REMOTE_START = 0x0631  # Remotely starts operation
    AL_TIME_OF_DAY = 0xF001  # Current local time
    AL_DATE = 0xF002  # Curent local date
    AL_MESSAGE_CENTER_NOTIFICATION = 0xF003  # Notification from message center
    AL_SWITCH_ENTITY_ON_OFF = (
        0xF101  # Entity control e.g. activate an alert or timer program
    )
    AL_INFO_SWITCH_ENTITY_ON_OFF = 0xF102  # Reflects the active state of an entity e.g. alert or timer program
    AL_CONSISTENCY_TAG = (
        0xF104  # Notifications of RF devices (e. g. Battery low)
    )
    AL_BATTERY_STATUS = (
        0xF105  # Notifications of RF devices (e. g. Battery low)
    )
    AL_STAY_AWAKE = 0xF106  # Notifications of RF devices (e. g. Battery low)
    AL_CYCLIC_SLEEP_TIME = 0xF10B  # Time of sleep cycles
    AL_SYSAP_PRESENCE = 0xF10C  # SysAP presence
    AL_SYSAP_TEMPERATURE = 0xF10D  # SysAP temperature
    AL_STANDBY_STATISTICS = (
        0xF10E  # Statistics about standby usage for battery devices
    )
    AL_HEARTBEAT_DELAY = 0xF10F  # Time period between two heartbeats
    AL_INFO_HEARTBEAT_DELAY = 0xF110  # Time period between two heartbeats
    AL_MEASURED_TEMPERATURE_1 = 0xFF01  # For debug purposes
    AL_MEASURED_TEMPERATURE_2 = 0xFF02  # For debug purposes
    AL_MEASURED_TEMPERATURE_3 = 0xFF03  # For debug purposes
    AL_MEASURED_TEMPERATURE_4 = 0xFF04  # For debug purposes
    AL_IGNORE = 0xFFFE  # Ignore this datapoint
    AL_INVALID = 0xFFFF  # Mark the datapoint as invalid
