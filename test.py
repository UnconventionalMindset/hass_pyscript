from pyscript_mock import *

import sys, os

if "/config/pyscript/modules" not in sys.path:
    sys.path.append("/config/pyscript/modules")

from sensor import *

corridorlight = 'light.corridorlight'
entrancelight = 'light.entrancelight'
entrancesensor_occupancy = 'binary_sensor.hueentrancesensor_occupancy'
corridorsensor_occupancy = 'binary_sensor.huecorridorsensor_occupancy'
entrance_timer="timer.entrance_timer"
corridor_timer="timer.corridor_timer"