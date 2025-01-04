from datetime import datetime

btn_step_down = 9  # Step to decrease brightness
dimming_delay_time_btn = 2
timeout_increase_btn = 1  # Initial timeout in seconds before dimming starts

log_label='input_text.log'
label='input_text.result'

sensors_dict = {
    "timer.entrance_timer": label,
    "timer.corridor_timer": ""
}


def get_seconds(timer):
    time_str = hass.states.get(timer).attributes.get('remaining')

    if not time_str:
        return 0

    time_obj = datetime.strptime(time_str, "%H:%M:%S")
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second

def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}:{minutes:02}:{seconds:02}"

def set_text(label, text):
    service.call(name="set_value", entity_id=label, value=text, domain='input_text')

def set_timer(timer, duration):
    service.call(name="start", domain="timer", entity_id=timer, duration=duration)


@service
def increase_timeout_btn(timer):
    global interrupted_btn
    current_timer_value = int(get_seconds(timer))

# hass.states.get("timer.entrance_timer").state
    new_time=format_time(current_timer_value + timeout_increase_btn)

    service.call(name="pause", domain="timer", entity_id=timer)
    state.set(timer, duration=new_time, remaining=new_time)

    set_text(log_label, f'Timeout increased to {new_time} seconds')
    set_text(label, '100')

@service
def start_dimming_btn(timer):
    global interrupted_btn
    # interrupted_btn = False
    # Start dimming the light
    brightness = 0
    
    state_value = hass.states.get('input_text.result').state
    try:
        brightness = int(state_value)
    except ValueError:
        brightness = 0

    # int((current_time / total_time) * 100)
    set_text(log_label, f"brightness: {brightness}")

    new_brightness = 0
    if brightness > 50:
        new_brightness = 50
    else:
        new_brightness = max(0, brightness - btn_step_down)
    
    set_text(label, new_brightness)
    set_text(log_label, f'Dimmed to {new_brightness}')

@state_trigger("timer.entrance_timer")
@state_active("timer.entrance_timer == 'active'")
def timer_completed():
    global interrupted_btn
    task.unique('dimming')
    start_dimming_btn('timer.entrance_timer')
    # service.call("persistent_notification", "create", title="Sensor changed", message='test1')

@state_trigger("timer.entrance_timer")
@state_active("timer.entrance_timer == 'idle'")
def ciao():
    light=sensors_dict.get("timer.entrance_timer")
    brightness=int(hass.states.get(light).state)
    if (brightness > 0):
        timer="timer.entrance_timer"
        timer_state = hass.states.get(timer).state
        timer_seconds_left = int(get_seconds(timer))
        if (timer_state != 'active' and timer_seconds_left != 0):
            set_timer(timer=timer, duration=timer_seconds_left)
        else:
            set_timer(timer, dimming_delay_time_btn)
    else:
        set_text(log_label, f'fully off')

        

@service
def handle_btn_sensor_triggered():
    # Turn the lights on and reset any timer
    increase_timeout_btn('timer.entrance_timer')

@service
def handle_btn_sensor_released():
    timer='timer.entrance_timer'
    
    timer_state = hass.states.get(timer).state
    timer_seconds_left = int(get_seconds(timer))
    if (timer_state != 'active' and timer_seconds_left != 0):
        set_timer(timer=timer, duration=timer_seconds_left)
    else:
        set_timer('timer.entrance_timer', dimming_delay_time_btn)


def get_seconds(timer):
    time_str = hass.states.get(timer).attributes.get('remaining')

    if not time_str:
        return 0

    time_obj = datetime.strptime(time_str, "%H:%M:%S")
    return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second

def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}:{minutes:02}:{seconds:02}"

def set_text(label, text):
    service.call(name="set_value", entity_id=label, value=text, domain='input_text')

def set_timer(timer, duration):
    service.call(name="start", domain="timer", entity_id=timer, duration=duration)
    

    # set_text('input_text.log', f"timer is: {hass.states.get('timer.entrance_timer').state}...")
    # if hass.states.get("timer.entrance_timer").state == 'idle':  # Check if the sensor was triggered again during the wait
    #     start_dimming_btn(label, 'timer.entrance_timer')




# @state_trigger("timer.entrance_timer")
# def my_entity_changed(**kwargs):
#   current_status = kwargs["value"]

#   message = f"Sensor changed to {current_status}."
#   service.call("persistent_notification", "create", title="Sensor changed", message=message)

# @state_trigger("timer.entrance_timer == 'idle'")
# def my_entity_change():
#   service.call("persistent_notification", "create", title="Sensor changed", message='test')





# btn_on = 'input_button.test_on'
# btn_off = 'input_button.test_off'
# btn_off = 'input_button.test_off'
# btn_off = 'input_button.test_off'

# @state_trigger(f"{btn_off}")
# def button_off():
#     handle_btn_sensor_released()

# @state_trigger(f"{btn_on}")
# def test():
#     handle_btn_sensor_triggered()

# @state_trigger
# service.call(name="start", domain="timer", entity_id="timer.entrance_timer", duration="20")