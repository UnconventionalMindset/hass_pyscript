from datetime import datetime

brightness_step_down = 50
dimming_delay_time = 15
increase_delay_amount = 5
initial_delay = 25
max_delay = 120

def get_seconds(timer):
    time_str = hass.states.get(timer).attributes.get("remaining")

    if not time_str:
        return 0

    time_obj = datetime.strptime(time_str, "%H:%M:%S")
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second

def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}:{minutes:02}:{seconds:02}"

def set_brightness(light_entity, new_brightness):
    light.turn_on(entity_id=light_entity, brightness=new_brightness)

def set_timer(timer, duration):
    service.call(name="start", domain="timer", entity_id=timer, duration=duration)

# Increases a delay every time the sensor is retriggered
def increase_delay(new_delay):
    increased_delay = new_delay + increase_delay_amount
    # Don't go over a certain threshold when increasing the delay
    return max_delay if increased_delay > max_delay else increased_delay

def pause_timer(timer):
    current_delay = int(get_seconds(timer))
    # If the current delay is higher than the initial, let's continue increasing
    new_delay = max(initial_delay, current_delay)
    new_time = format_time(increase_delay(new_delay))
    service.call(name="pause", domain="timer", entity_id=timer)
    state.set(timer, duration=new_time, remaining=new_time)
    log.info(f"Delay increased from {current_delay} to {new_time} seconds")

def dim(old_brightness):
    if old_brightness > 50:
        return 50

    return max(0, old_brightness - brightness_step_down)

def keep_dimming(timer):
    timer_state = hass.states.get(timer).state
    timer_seconds_left = int(get_seconds(timer))

    new_delay = 0
    if timer_state == "active" or timer_seconds_left == 0:
        new_delay = dimming_delay_time
    else:
        new_delay = timer_seconds_left

    set_timer(timer, new_delay)
    log.info(f"Delay before next brightness decrease: {new_delay}")

def timer_stopped(timer, light):
    old_brightness = int(hass.states.get(light).attributes.get("brightness") or 0)
    new_brightness = dim(old_brightness)

    if (old_brightness <= 0 or new_brightness <= 0):
        # No timer needed anymore if light is off or area is too bright
        set_brightness(light, 0)
        log.info(f"Light {light} is now fully off")
        return

    set_brightness(light, new_brightness)
    log.info(f"Dimmed {light} from {old_brightness} to {new_brightness} due to movement absence")
    keep_dimming(timer)

def motion_detected(timer, light, illuminance):
    # Turn the lights on and reset any timer
    pause_timer(timer)

    if (int(state.get(illuminance)) > 25):
        log.info(f"Motion trigger for {light} ignored since ambient light it's good enough")
        return

    set_brightness(light, "255")
    log.info(f"Turned on {light} due to sensor movement")

def motion_absent(timer):
    keep_dimming(timer)