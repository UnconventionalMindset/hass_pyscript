"""Motion sensor automation for manual brightness control via input text entities.

This module provides functions for controlling lights based on timer states and
manual brightness input through Home Assistant input_text entities.
"""

from datetime import datetime

# Configuration
CONFIG = {
    'brightness_step_down': 9,      # Step to decrease brightness
    'dimming_delay': 2,             # Delay between dimming steps in seconds
    'timeout_increase': 1,          # Initial timeout increase in seconds
    'entities': {
        'log_label': 'input_text.log',
        'brightness_label': 'input_text.result',
        'entrance_timer': 'timer.entrance_timer',
        'corridor_timer': 'timer.corridor_timer'
    },
    'timer_to_light_mapping': {
        'timer.entrance_timer': 'input_text.result',
        'timer.corridor_timer': ''
    }
}

def get_timer_remaining_seconds(timer_entity):
    """Get remaining seconds from a timer entity.
    
    Args:
        timer_entity: Timer entity ID
        
    Returns:
        int: Remaining seconds, 0 if timer is not active or invalid
    """
    try:
        timer_state = hass.states.get(timer_entity)
        if not timer_state:
            return 0
            
        time_str = timer_state.attributes.get('remaining')
        if not time_str:
            return 0

        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
    except (ValueError, AttributeError) as e:
        log.warning(f"Error getting timer seconds for {timer_entity}: {e}")
        return 0

def format_duration(seconds):
    """Convert seconds to HH:MM:SS format.
    
    Args:
        seconds: Duration in seconds
        
    Returns:
        str: Formatted duration string
    """
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}:{minutes:02d}:{seconds:02d}"

def set_input_text(entity_id, value):
    """Set value of an input_text entity.
    
    Args:
        entity_id: Input text entity ID
        value: Value to set
    """
    try:
        service.call(name="set_value", entity_id=entity_id, value=str(value), domain='input_text')
        log.debug(f"Set {entity_id} to {value}")
    except Exception as e:
        log.error(f"Failed to set {entity_id} to {value}: {e}")

def start_timer(timer_entity, duration):
    """Start a timer with specified duration.
    
    Args:
        timer_entity: Timer entity ID
        duration: Duration in seconds or formatted string
    """
    try:
        if isinstance(duration, int):
            duration_str = format_duration(duration)
        else:
            duration_str = str(duration)
            
        service.call(name="start", domain="timer", entity_id=timer_entity, duration=duration_str)
        log.debug(f"Started timer {timer_entity} for {duration_str}")
    except Exception as e:
        log.error(f"Failed to start timer {timer_entity}: {e}")

def get_brightness_from_input():
    """Get current brightness value from input text entity.
    
    Returns:
        int: Brightness value, 0 if invalid or not found
    """
    try:
        brightness_state = hass.states.get(CONFIG['entities']['brightness_label'])
        if not brightness_state:
            return 0
        return int(brightness_state.state)
    except (ValueError, AttributeError):
        log.warning(f"Invalid brightness value in {CONFIG['entities']['brightness_label']}")
        return 0

def calculate_next_brightness(current_brightness):
    """Calculate next brightness level after dimming.
    
    Args:
        current_brightness: Current brightness value
        
    Returns:
        int: Next brightness level
    """
    if current_brightness > 50:
        return 50
    return max(0, current_brightness - CONFIG['brightness_step_down'])

def pause_and_extend_timer(timer_entity, additional_time):
    """Pause timer and extend its duration.
    
    Args:
        timer_entity: Timer entity ID
        additional_time: Additional time to add in seconds
    """
    try:
        current_time = get_timer_remaining_seconds(timer_entity)
        new_time = format_duration(current_time + additional_time)
        
        service.call(name="pause", domain="timer", entity_id=timer_entity)
        state.set(timer_entity, duration=new_time, remaining=new_time)
        
        set_input_text(CONFIG['entities']['log_label'], f'Timeout increased to {new_time}')
        set_input_text(CONFIG['entities']['brightness_label'], '100')
        
        log.info(f"Extended timer {timer_entity} by {additional_time}s to {new_time}")
    except Exception as e:
        log.error(f"Failed to extend timer {timer_entity}: {e}")

def dim_brightness():
    """Dim the brightness based on current input value."""
    try:
        current_brightness = get_brightness_from_input()
        next_brightness = calculate_next_brightness(current_brightness)
        
        set_input_text(CONFIG['entities']['log_label'], f"brightness: {current_brightness}")
        set_input_text(CONFIG['entities']['brightness_label'], str(next_brightness))
        set_input_text(CONFIG['entities']['log_label'], f'Dimmed to {next_brightness}')
        
        log.info(f"Dimmed brightness: {current_brightness} → {next_brightness}")
    except Exception as e:
        log.error(f"Failed to dim brightness: {e}")

def handle_timer_restart(timer_entity):
    """Handle timer restart logic based on current state.
    
    Args:
        timer_entity: Timer entity ID
    """
    try:
        timer_state = hass.states.get(timer_entity)
        if not timer_state:
            log.warning(f"Timer {timer_entity} not found")
            return
            
        timer_seconds_left = get_timer_remaining_seconds(timer_entity)
        
        if timer_state.state != 'active' and timer_seconds_left > 0:
            duration = timer_seconds_left
        else:
            duration = CONFIG['dimming_delay']
            
        start_timer(timer_entity, duration)
        log.debug(f"Restarted timer {timer_entity} with duration {duration}s")
    except Exception as e:
        log.error(f"Failed to handle timer restart for {timer_entity}: {e}")

# Service functions for external calls
@service
def increase_timeout_sensor(timer_entity=None):
    """Increase timeout for motion sensor timer.
    
    Args:
        timer_entity: Timer entity ID (defaults to entrance timer)
    """
    if not timer_entity:
        timer_entity = CONFIG['entities']['entrance_timer']
    pause_and_extend_timer(timer_entity, CONFIG['timeout_increase'])

@service
def start_dimming_sensor(timer_entity=None):
    """Start dimming sequence for motion sensor.
    
    Args:
        timer_entity: Timer entity ID (defaults to entrance timer)
    """
    if not timer_entity:
        timer_entity = CONFIG['entities']['entrance_timer']
    task.unique('dimming')
    dim_brightness()

@service
def handle_motion_sensor_triggered():
    """Handle motion sensor activation."""
    increase_timeout_sensor(CONFIG['entities']['entrance_timer'])

@service
def handle_motion_sensor_released():
    """Handle motion sensor deactivation."""
    handle_timer_restart(CONFIG['entities']['entrance_timer'])

# State triggers for entrance timer
@state_trigger("timer.entrance_timer")
@state_active("timer.entrance_timer == 'active'")
def entrance_timer_active():
    """Handle entrance timer becoming active."""
    start_dimming_sensor('timer.entrance_timer')

@state_trigger("timer.entrance_timer")
@state_active("timer.entrance_timer == 'idle'")
def entrance_timer_idle():
    """Handle entrance timer becoming idle."""
    try:
        light_entity = CONFIG['timer_to_light_mapping'].get('timer.entrance_timer')
        if not light_entity:
            log.warning("No light entity mapped for timer.entrance_timer")
            return
            
        brightness = get_brightness_from_input()
        
        if brightness > 0:
            handle_timer_restart('timer.entrance_timer')
        else:
            set_input_text(CONFIG['entities']['log_label'], 'fully off')
            log.info("Timer idle: brightness is 0, keeping lights off")
    except Exception as e:
        log.error(f"Failed to handle timer idle state: {e}")