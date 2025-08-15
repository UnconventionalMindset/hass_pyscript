import sys, os

if "/config/pyscript/modules" not in sys.path:
    sys.path.append("/config/pyscript/modules")

from light_controls import *

def hold_light_on(conditions):
    for hold_light_on_condition in conditions:
        if state.get(hold_light_on_condition['entity']) == hold_light_on_condition['expected_state']:
            return True
    return False

registered_triggers = []

def make_motion_light(config):
    motion_sensor = config['motion_sensor']
    light = config['light']
    timer = config['timer']
    illuminance = config['illuminance']
    hold_light_on_conditions = config['hold_light_on_conditions']

    @state_trigger(f"{timer}")
    @state_active(f"{timer} == 'idle'")
    def motion_light_timer_stopped():
        if hold_light_on(hold_light_on_conditions):
            log.info(f"Light {light} is being kept on.")
            return

        task.unique(f"motion_light_timer_stopped_{timer}")
        log.info(f"Timer {timer} stopped, starting unique task...")
        handle_timer_finished(timer, light)

    @state_trigger(f"{motion_sensor} == 'on'")
    def motion_light_motion_detected():
        if hold_light_on(hold_light_on_conditions):
            log.info(f"Light {light} is being kept on.")
            return
        
        task.unique(f"motion_light_motion_detected_{motion_sensor}")
        log.info(f"Motion from {motion_sensor} detected, starting unique task...")
        handle_motion_detected(timer, light, illuminance)

    @state_trigger(f"{motion_sensor} == 'off'")
    def motion_light_motion_absent():
        if hold_light_on(hold_light_on_conditions):
            log.info(f"Light {light} is being kept on.")
            return

        task.unique(f"motion_light_motion_absent_{motion_sensor}")
        log.info(f"Motion from {motion_sensor} absent, starting unique task...")
        handle_motion_cleared(timer)

    registered_triggers.append(motion_light_timer_stopped)
    registered_triggers.append(motion_light_motion_detected)
    registered_triggers.append(motion_light_motion_absent)

@time_trigger('startup')
def motion_light_startup():
    for app in pyscript.app_config:
        make_motion_light(app)