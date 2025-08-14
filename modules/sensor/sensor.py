"""Motion-activated lighting sensor utilities with time-aware functionality.

Provides functions for intelligent light control with motion detection,
gradual dimming, and nighttime awareness.
"""

from datetime import datetime

# Configuration constants
BRIGHTNESS_STEP_DOWN = 50
DAYTIME_DIMMING_DELAY = 15
NIGHTTIME_DIMMING_DELAY = 0  # Immediate dimming between midnight and 6am
INCREASE_DELAY_AMOUNT = 5
DAYTIME_INITIAL_DELAY = 25
NIGHTTIME_INITIAL_DELAY = 0  # No delay between midnight and 6am
MAX_DELAY = 120
NIGHTTIME_START_HOUR = 0
NIGHTTIME_END_HOUR = 6
ILLUMINANCE_THRESHOLD = 25
MAX_BRIGHTNESS = 255
MID_BRIGHTNESS = 50

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

def is_nighttime():
    """Check if current time is within nighttime hours.
    
    Returns:
        bool: True if between midnight and 6am
    """
    current_hour = datetime.now().hour
    return NIGHTTIME_START_HOUR <= current_hour < NIGHTTIME_END_HOUR

def get_initial_delay():
    """Get the appropriate initial delay based on current time.
    
    Returns:
        int: Initial delay in seconds
    """
    return NIGHTTIME_INITIAL_DELAY if is_nighttime() else DAYTIME_INITIAL_DELAY

def get_dimming_delay():
    """Get the appropriate dimming delay based on current time.
    
    Returns:
        int: Dimming delay in seconds
    """
    return NIGHTTIME_DIMMING_DELAY if is_nighttime() else DAYTIME_DIMMING_DELAY

def calculate_increased_delay(current_delay):
    """Calculate increased delay with maximum threshold.
    
    Args:
        current_delay: Current delay value in seconds
        
    Returns:
        int: New delay value, capped at maximum
    """
    increased_delay = current_delay + INCREASE_DELAY_AMOUNT
    return min(increased_delay, MAX_DELAY)

def pause_and_extend_timer(timer_entity):
    """Pause timer and extend duration based on activity.
    
    Args:
        timer_entity: Timer entity ID
    """
    current_delay = get_timer_remaining_seconds(timer_entity)
    time_based_initial_delay = get_initial_delay()
    
    # Use higher of current delay or initial delay, then increase
    base_delay = max(time_based_initial_delay, current_delay)
    new_delay = calculate_increased_delay(base_delay)
    new_duration = format_duration(new_delay)
    
    # Pause timer and set new duration
    timer.pause(entity_id=timer_entity)
    state.set(timer_entity, duration=new_duration, remaining=new_duration)
    
    mode = "nighttime" if is_nighttime() else "daytime"
    log.info(f"Extended timer {timer_entity} from {current_delay}s to {new_delay}s ({mode} mode)")

def calculate_dimmed_brightness(current_brightness):
    """Calculate next dimming step for brightness.
    
    Args:
        current_brightness: Current brightness level
        
    Returns:
        int: New brightness level (0-255)
    """
    if current_brightness > MID_BRIGHTNESS:
        return MID_BRIGHTNESS
    
    return max(0, current_brightness - BRIGHTNESS_STEP_DOWN)

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
    nighttime_mode = is_nighttime()
    
    if timer_state.state == "active" or timer_seconds_left == 0:
        delay = get_dimming_delay()
        mode = "nighttime" if nighttime_mode else "daytime"
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
    new_brightness = calculate_dimmed_brightness(current_brightness)

    if current_brightness <= 0 or new_brightness <= 0:
        set_light_brightness(light_entity, 0)
        log.info(f"Light {light_entity} turned off (final dimming step)")
        return

    set_light_brightness(light_entity, new_brightness)
    log.info(f"Dimmed {light_entity}: {current_brightness} → {new_brightness}")
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
    current_illuminance = int(state.get(illuminance_entity) or 0)
    if current_illuminance > ILLUMINANCE_THRESHOLD:
        log.info(f"Motion ignored for {light_entity} - sufficient ambient light ({current_illuminance} lux)")
        return

    set_light_brightness(light_entity, MAX_BRIGHTNESS)
    log.info(f"Motion detected: turned on {light_entity}")

def handle_motion_cleared(timer_entity):
    """Handle motion clearing event.
    
    Args:
        timer_entity: Timer entity ID
    """
    schedule_next_dimming(timer_entity)