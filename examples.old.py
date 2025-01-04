from pyscript_mock import *

import sys, os

if "/config/pyscript/modules" not in sys.path:
    sys.path.append("/config/pyscript/modules")

# def list_directories(path):
#     directories = []
#     for dirpath, dirnames, filenames in os.walk(path):
#         directories.append(dirpath)
#     return directories

# for directory in list_directories("/config/pyscript/modules"):
#     log.info(f" s - {directory}")
from sensor import *
# from utils import now
# import asyncio
# asyncio.sleep

# binary_sensor_light_control.py

# Global variables for timer and brightness
corridorlight = 'light.corridorlight'
entrancelight = 'light.entrancelight'
entrancesensor_occupancy = 'binary_sensor.hueentrancesensor_occupancy'
corridorsensor_occupancy = 'binary_sensor.huecorridorsensor_occupancy'
entrance_timer="timer.entrance_timer"
corridor_timer="timer.corridor_timer"

# # Listen to binary sensor state changes
# @state_trigger(f"{entrancesensor_occupancy} == 'on'")
# def entrancesensor_on():
#     person_detected(entrance_timer)

# @state_trigger(f"{entrancesensor_occupancy} == 'off'")
# def entrancesensor_off():
#     person_absent(entrance_timer)

# @state_trigger(f"{corridorsensor_occupancy} == 'on'")
# def corridorsensor_on():
#     person_detected(corridor_timer)

# @state_trigger(f"{corridorsensor_occupancy} == 'off'")
# def corridorsensor_off():
#     person_absent(corridor_timer)

# from homeassistant.const import EVENT_CALL_SERVICE
# @event_trigger(EVENT_CALL_SERVICE)
# def monitor_service_calls(**kwargs):
#     entity = kwargs['service_data']['entity_id']
#     if (entity == entrance_timer and ):

#         log.info(f"got EVENT_CALL_SERVICE with kwargs={kwargs['service_data']['entity_id']}")
#         # if "name" in my_dict:


# from homeassistant.const import EVENT_STATE_CHANGED
# @event_trigger(EVENT_STATE_CHANGED)
# def monitor_service_calls(**kwargs):
#     # log.info(f"got EVENT_CALL_SERVICE with kwargs={kwargs}")
#     entity = kwargs['entity_id']
#     new_state = kwargs['new_state'].state
#     if (entity in sensors_dict and new_state == "idle"):
#         timer_stopped(entity)


# def timer_started(timer):
#     # Starts dimming
#     light = sensors_dict.get(timer)
#     old_brightness = int(hass.states.get(light).attributes.get('brightness') or 0)
#     new_brightness = dim(old_brightness)
    
#     set_brightness(light, new_brightness)
#     log.info(f'Dimmed {light} from {old_brightness} to {new_brightness}')