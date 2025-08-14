"""Motion-activated lighting sensor utilities with time-aware functionality.

Provides functions for intelligent light control with motion detection,
gradual dimming, and nighttime awareness.
"""

from datetime import datetime

# Configuration constants
CONFIG = {
    'daytime': {
        'initial_delay': 25,
        'dimming_delay': 15,
        'brightness_levels': [255, 50, 0],  # Full -> Mid -> Off
    },
    'nighttime': {
        'initial_delay': 0,
        'dimming_delay': 0,
        'brightness_levels': [170, 1, 0],   # Medium -> Min -> Off
        'min_brightness_delay': 6
    },
    'general': {
        'increase_delay_amount': 5,
        'max_delay': 120,
        'nighttime_hours': (0, 6),
        'illuminance_threshold': 25
    }
}

def get_timer_remaining_seconds(timer_entity):
    """Get remaining seconds from a timer entity.
    
    Args:
        timer_entity: Timer entity ID
        
    Returns:
        int: Remaining seconds, 0 if timer is not active
    """
    timer_state = hass.states.get(timer_entity)
    if not timer_state:
        return 0
        
    time_str = timer_state.attributes.get("remaining")
    if not time_str:
        return 0

    try:
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        return time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
    except ValueError:
        log.warning(f"Invalid timer format for {timer_entity}: {time_str}")
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

def set_light_brightness(light_entity, brightness):
    """Set light brightness using pyscript service call.
    
    Args:
        light_entity: Light entity ID
        brightness: Brightness value (0-255) or string
    """
    light.turn_on(entity_id=light_entity, brightness=int(brightness))
    log.debug(f"Set {light_entity} brightness to {brightness}")

def start_timer(timer_entity, duration_seconds):
    """Start a timer with specified duration.
    
    Args:
        timer_entity: Timer entity ID
        duration_seconds: Duration in seconds or formatted string
    """
    if isinstance(duration_seconds, int):
        duration_str = format_duration(duration_seconds)
    else:
        duration_str = duration_seconds
        
    timer.start(entity_id=timer_entity, duration=duration_str)
    log.debug(f"Started timer {timer_entity} for {duration_str}")

def get_time_mode():
    """Get current time mode configuration.
    
    Returns:
        str: 'nighttime' or 'daytime'
    """
    current_hour = datetime.now().hour
    start, end = CONFIG['general']['nighttime_hours']
    return 'nighttime' if start <= current_hour < end else 'daytime'

def get_config(key):
    """Get configuration value for current time mode.
    
    Args:
        key: Configuration key
        
    Returns:
        Configuration value for current time mode
    """
    mode = get_time_mode()
    return CONFIG[mode].get(key, CONFIG['general'].get(key))

def calculate_increased_delay(current_delay):
    """Calculate increased delay with maximum threshold.
    
    Args:
        current_delay: Current delay value in seconds
        
    Returns:
        int: New delay value, capped at maximum
    """
    increased_delay = current_delay + CONFIG['general']['increase_delay_amount']
    return min(increased_delay, CONFIG['general']['max_delay'])

def pause_and_extend_timer(timer_entity):
    """Pause timer and extend duration based on activity.
    
    Args:
        timer_entity: Timer entity ID
    """
    current_delay = get_timer_remaining_seconds(timer_entity)
    initial_delay = get_config('initial_delay')
    
    # Use higher of current delay or initial delay, then increase
    base_delay = max(initial_delay, current_delay)
    new_delay = calculate_increased_delay(base_delay)
    new_duration = format_duration(new_delay)
    
    # Pause timer and set new duration
    timer.pause(entity_id=timer_entity)
    state.set(timer_entity, duration=new_duration, remaining=new_duration)
    
    mode = get_time_mode()
    log.info(f"Extended timer {timer_entity} from {current_delay}s to {new_delay}s ({mode} mode)")

def get_next_brightness_level(current_brightness):
    """Get next brightness level in the dimming sequence.
    
    Args:
        current_brightness: Current brightness level
        
    Returns:
        int: Next brightness level in sequence
    """
    brightness_levels = get_config('brightness_levels')
    
    # Find the next lower brightness level
    for i, level in enumerate(brightness_levels):
        if current_brightness > level:
            return level
    
    # If we're at or below the lowest level, turn off
    return 0

def schedule_next_dimming(timer_entity):
    """Schedule the next dimming cycle.
    
    Args:
        timer_entity: Timer entity ID
    """
    timer_state = hass.states.get(timer_entity)
    if not timer_state:
        log.warning(f"Timer entity {timer_entity} not found")
        return
        
    timer_seconds_left = get_timer_remaining_seconds(timer_entity)
    mode = get_time_mode()
    
    if timer_state.state == "active" or timer_seconds_left == 0:
        delay = get_config('dimming_delay') or 1  # Use 1 second minimum
        log.info(f"Using {mode} dimming delay: {delay} seconds")
    else:
        delay = timer_seconds_left
        log.debug(f"Continuing with existing timer: {delay} seconds")

    start_timer(timer_entity, delay)

def handle_timer_finished(timer_entity, light_entity):
    """Handle timer completion by dimming light and scheduling next cycle.
    
    Args:
        timer_entity: Timer entity ID
        light_entity: Light entity ID
    """
    light_state = hass.states.get(light_entity)
    if not light_state:
        log.warning(f"Light entity {light_entity} not found")
        return
        
    current_brightness = int(light_state.attributes.get("brightness") or 0)
    next_brightness = get_next_brightness_level(current_brightness)
    mode = get_time_mode()
    
    log.debug(f"{mode.title()}: current={current_brightness}, next={next_brightness}")
    
    if next_brightness <= 0:
        set_light_brightness(light_entity, 0)
        log.info(f"{mode.title()}: turned off {light_entity}")
        return
    
    set_light_brightness(light_entity, next_brightness)
    log.info(f"{mode.title()}: dimmed {light_entity}: {current_brightness} → {next_brightness}")
    
    # Schedule next step with appropriate delay
    if mode == 'nighttime' and next_brightness == 1:
        # Special case: nighttime minimum brightness delay
        delay = get_config('min_brightness_delay')
        log.info(f"Nighttime: waiting {delay}s at minimum brightness before turning off")
        start_timer(timer_entity, delay)
    else:
        schedule_next_dimming(timer_entity)

def handle_motion_detected(timer_entity, light_entity, illuminance_entity):
    """Handle motion detection event.
    
    Args:
        timer_entity: Timer entity ID
        light_entity: Light entity ID  
        illuminance_entity: Illuminance sensor entity ID
    """
    pause_and_extend_timer(timer_entity)

    # Check ambient light level
    illuminance_value = state.get(illuminance_entity)
    try:
        current_illuminance = int(illuminance_value) if illuminance_value not in [None, 'unknown', 'unavailable'] else 0
    except (ValueError, TypeError):
        current_illuminance = 0
        log.warning(f"Invalid illuminance value '{illuminance_value}' for {illuminance_entity}, using 0")
    
    threshold = CONFIG['general']['illuminance_threshold']
    if current_illuminance > threshold:
        log.info(f"Motion ignored for {light_entity} - sufficient ambient light ({current_illuminance} lux)")
        return

    # Turn on at maximum brightness (first level in sequence)
    max_brightness = get_config('brightness_levels')[0]
    set_light_brightness(light_entity, max_brightness)
    log.info(f"Motion detected: turned on {light_entity}")

def handle_motion_cleared(timer_entity):
    """Handle motion clearing event.
    
    Args:
        timer_entity: Timer entity ID
    """
    mode = get_time_mode()
    initial_delay = get_config('initial_delay')
    
    if initial_delay == 0:
        # Immediate dimming (typically nighttime)
        start_timer(timer_entity, 1)  # Use 1 second minimum
        log.info(f"{mode.title()} motion cleared: immediate dimming for {timer_entity}")
    else:
        # Standard delay behavior
        start_timer(timer_entity, initial_delay)
        log.info(f"{mode.title()} motion cleared: {initial_delay}s delay for {timer_entity}")


# Backward compatibility aliases for existing apps  
def motion_detected(timer, light, illuminance):
    """Backward compatibility wrapper for handle_motion_detected."""
    handle_motion_detected(timer, light, illuminance)

def motion_absent(timer):
    """Backward compatibility wrapper for handle_motion_cleared."""
    handle_motion_cleared(timer)

def timer_stopped(timer, light):
    """Backward compatibility wrapper for handle_timer_finished."""
    handle_timer_finished(timer, light)