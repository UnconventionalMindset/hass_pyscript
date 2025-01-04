# fmt:off
from typing import Any, Literal

class _entity:
    last_changed: Any
    entity_id: Any
    last_updated: Any

class androidtv:

    @staticmethod
    def adb_command(*, entity_id: str, command: str):
        """
        Sends an ADB command to an Android / Fire TV device.
        :param command: Either a key command or an ADB shell command.
        """
        ...

    @staticmethod
    def learn_sendevent(*, entity_id: str):
        """
        Translates a key press on a remote into ADB 'sendevent' commands. You must press one button on the remote within 8 seconds of performing this action.
        """
        ...

    @staticmethod
    def download(*, entity_id: str, device_path: str, local_path: str):
        """
        Downloads a file from your Android / Fire TV device to your Home Assistant instance.
        :param device_path: The filepath on the Android / Fire TV device.
        :param local_path: The filepath on your Home Assistant instance.
        """
        ...

    @staticmethod
    def upload(*, entity_id: str, device_path: str, local_path: str):
        """
        Uploads a file from your Home Assistant instance to an Android / Fire TV device.
        :param device_path: The filepath on the Android / Fire TV device.
        :param local_path: The filepath on your Home Assistant instance.
        """
        ...

class automation_entity(_entity):
    current: Any
    friendly_name: Any
    icon: Any
    id: Any
    last_triggered: Any
    mode: Any
    restored: Any
    supported_features: Any

    def trigger(self, *, skip_condition: bool=False):
        """
        Triggers the actions of an automation.
        :param skip_condition: Defines whether or not the conditions will be skipped.
        """
        ...

    def toggle(self):
        """
        Toggles (enable / disable) an automation.
        """
        ...

    def turn_on(self):
        """
        Enables an automation.
        """
        ...

    def turn_off(self, *, stop_actions: bool=False):
        """
        Disables an automation.
        :param stop_actions: Stops currently running actions.
        """
        ...

class automation:
    new_automation = automation_entity()
    bedrdialincr = automation_entity()
    hometoggle = automation_entity()
    homeon = automation_entity()
    diallivingincr = automation_entity()
    livingdialdecr = automation_entity()
    standinglamp = automation_entity()
    radio = automation_entity()
    radio_gtv = automation_entity()
    bedrtoggle = automation_entity()
    corridortoggle = automation_entity()
    livingdialdecr_2 = automation_entity()
    livingdialincr = automation_entity()
    corridortoggle_2 = automation_entity()
    nightstandlights = automation_entity()
    diningtoggle = automation_entity()
    livingdialdecrfast = automation_entity()
    livingdialincrfast = automation_entity()
    bedrdialdecrslow = automation_entity()
    bedrdialdecrfast = automation_entity()
    livingtoggle = automation_entity()
    livingreset = automation_entity()
    bedrdialincrfast = automation_entity()
    bedrdialincrslow = automation_entity()
    bedroomscenes = automation_entity()
    bedroomreset = automation_entity()
    bedrdialincrslow_2 = automation_entity()
    bedrdialdecrstep = automation_entity()
    bedrdialdecrstep_2 = automation_entity()
    livingdialincrstep = automation_entity()
    nl = automation_entity()
    officetoggle = automation_entity()
    bedroomon100 = automation_entity()
    officeincrfast = automation_entity()
    officeincrslow = automation_entity()
    officedecrfast = automation_entity()
    officedialdecrslow = automation_entity()
    living_room_scenes = automation_entity()
    firetv_play_relaxing_music = automation_entity()
    openingfront = automation_entity()
    frontclosed = automation_entity()
    corridorsensor = automation_entity()
    entrancesensorreleased = automation_entity()
    corridorsensorreleased = automation_entity()
    entrancesensortriggered = automation_entity()
    kitchenonfp2sensor = automation_entity()
    kitchenarea = automation_entity()
    diningareafp2sensor = automation_entity()
    diningonfp2sensor = automation_entity()
    iriswithtv = automation_entity()
    iriswithtvoff = automation_entity()
    corridorholdaction = automation_entity()
    firetv_idle_turnsnoff_tv = automation_entity()

    @staticmethod
    def trigger(*, entity_id: str, skip_condition: bool=False):
        """
        Triggers the actions of an automation.
        :param skip_condition: Defines whether or not the conditions will be skipped.
        """
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """
        Toggles (enable / disable) an automation.
        """
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """
        Enables an automation.
        """
        ...

    @staticmethod
    def turn_off(*, entity_id: str, stop_actions: bool=False):
        """
        Disables an automation.
        :param stop_actions: Stops currently running actions.
        """
        ...

    @staticmethod
    def reload():
        """
        Reloads the automation configuration.
        """
        ...

class backup:

    @staticmethod
    def create():
        """
        Creates a new backup.
        """
        ...

class binary_sensor_entity(_entity):
    battery: Any
    contact: Any
    device_class: Any
    friendly_name: Any
    icon: Any
    illuminance: Any
    illuminance_lux: Any
    led_indication: Any
    linkquality: Any
    motion_sensitivity: Any
    occupancy: Any
    occupancy_timeout: Any
    restored: Any
    supported_features: Any
    temperature: Any
    update: Any
    update_available: Any

class binary_sensor:
    zigbee2mqtt_bridge_connection_state = binary_sensor_entity()
    arris_tg3492lg_sr_wan_status = binary_sensor_entity()
    zigbee2mqtt_bridge_connection_state_2 = binary_sensor_entity()
    zigbee2mqtt_bridge_connection_state_3 = binary_sensor_entity()
    athom_homelabsmartplug_status = binary_sensor_entity()
    athom_officesmartplug_status = binary_sensor_entity()
    athom_livingsmartplug_status = binary_sensor_entity()
    rocky_mop_attached = binary_sensor_entity()
    rocky_water_box_attached = binary_sensor_entity()
    rocky_water_shortage = binary_sensor_entity()
    rocky_cleaning = binary_sensor_entity()
    frontdoor_contact = binary_sensor_entity()
    iphone_focus = binary_sensor_entity()
    hueentrancesensor_occupancy = binary_sensor_entity()
    huecorridorsensor_occupancy = binary_sensor_entity()
    corridorwallfp2detection = binary_sensor_entity()
    corridorwallfp2diningarea = binary_sensor_entity()
    corridorwallfp2kitchenarea = binary_sensor_entity()
    slzb_06_ethernet = binary_sensor_entity()
    slzb_06_internet = binary_sensor_entity()

class button_entity(_entity):
    battery: Any
    brightness: Any
    contact: Any
    device_class: Any
    friendly_name: Any
    humidity: Any
    icon: Any
    linkquality: Any
    pm25: Any
    power_on_behavior: Any
    restored: Any
    supported_features: Any
    temperature: Any
    update: Any
    update_available: Any
    voc_index: Any

    def press(self):
        """
        Press the button entity.
        """
        ...

class button:
    zigbee2mqtt_bridge_restart = button_entity()
    zigbee2mqtt_bridge_restart_2 = button_entity()
    zigbee2mqtt_bridge_restart_3 = button_entity()
    athom_homelabsmartplug_restart_with_factory_default_settings = button_entity()
    athom_homelabsmartplug_safe_mode = button_entity()
    athom_officesmartplug_restart_with_factory_default_settings = button_entity()
    athom_officesmartplug_safe_mode = button_entity()
    athom_livingsmartplug_restart_with_factory_default_settings = button_entity()
    athom_livingsmartplug_safe_mode = button_entity()
    breatherboi_identify = button_entity()
    frontdoor_identify = button_entity()
    presence_sensor_fp2_56ed_identify = button_entity()
    wardrobelightsleftcontroller_identify = button_entity()
    wardrobelightsrightcontroller_identify = button_entity()
    slzb_06_core_restart = button_entity()
    slzb_06_zigbee_restart = button_entity()

    @staticmethod
    def press(*, entity_id: str):
        """
        Press the button entity.
        """
        ...

class cast:

    @staticmethod
    def show_lovelace_view(*, entity_id, dashboard_path: str, view_path: str=''):
        """
        Shows a dashboard view on a Chromecast device.
        :param entity_id: Media player entity to show the dashboard view on.
        :param dashboard_path: The URL path of the dashboard to show.
        :param view_path: The path of the dashboard view to show.
        """
        ...

class cloud:

    @staticmethod
    def remote_connect():
        """
        Makes the instance UI accessible from outside of the local network by using Home Assistant Cloud.
        """
        ...

    @staticmethod
    def remote_disconnect():
        """
        Disconnects the Home Assistant UI from the Home Assistant Cloud. You will no longer be able to access your Home Assistant instance from outside your local network.
        """
        ...

class conversation:

    @staticmethod
    def process(*, text: str, language: str='', agent_id=None, conversation_id: str='') -> dict[str, Any]:
        """
        Launches a conversation from a transcribed text.
        :param text: Transcribed text input.
        :param language: Language of text. Defaults to server language.
        :param agent_id: Conversation agent to process your request. The conversation agent is the brains of your assistant. It processes the incoming text commands.
        :param conversation_id: ID of the conversation, to be able to continue a previous conversation
        """
        ...

    @staticmethod
    def reload(*, language: str='', agent_id=None):
        """
        Reloads the intent configuration.
        :param language: Language to clear cached intents for. Defaults to server language.
        :param agent_id: Conversation agent to reload.
        """
        ...

class counter_entity(_entity):
    editable: Any
    friendly_name: Any
    icon: Any
    initial: Any
    maximum: Any
    minimum: Any
    step: Any

    def increment(self):
        """
        Increments a counter.
        """
        ...

    def decrement(self):
        """
        Decrements a counter.
        """
        ...

    def reset(self):
        """
        Resets a counter.
        """
        ...

    def set_value(self, *, value: int):
        """
        Sets the counter value.
        :param value: The new counter value the entity should be set to.
        """
        ...

class counter:
    counter = counter_entity()
    corridorincreasedelay = counter_entity()

    @staticmethod
    def increment(*, entity_id: str):
        """
        Increments a counter.
        """
        ...

    @staticmethod
    def decrement(*, entity_id: str):
        """
        Decrements a counter.
        """
        ...

    @staticmethod
    def reset(*, entity_id: str):
        """
        Resets a counter.
        """
        ...

    @staticmethod
    def set_value(*, entity_id: str, value: int):
        """
        Sets the counter value.
        :param value: The new counter value the entity should be set to.
        """
        ...

class device_tracker_entity(_entity):
    altitude: Any
    battery_level: Any
    course: Any
    friendly_name: Any
    gps_accuracy: Any
    latitude: Any
    longitude: Any
    source_type: Any
    speed: Any
    vertical_accuracy: Any

class device_tracker:
    note10_1_2 = device_tracker_entity()
    pixel_8 = device_tracker_entity()
    waydroid_spectre = device_tracker_entity()
    redmi = device_tracker_entity()
    oneplus_watch_2 = device_tracker_entity()
    xiaomi14 = device_tracker_entity()
    iphone = device_tracker_entity()

    @staticmethod
    def see(*, mac: str='', dev_id: str='', host_name: str='', location_name: str='', gps=None, gps_accuracy: int=0, battery: int=0):
        """
        Records a seen tracked device.
        :param mac: MAC address of the device.
        :param dev_id: ID of the device (find the ID in `known_devices.yaml`).
        :param host_name: Hostname of the device.
        :param location_name: Name of the location where the device is located. The options are: `home`, `not_home`, or the name of the zone.
        :param gps: GPS coordinates where the device is located, specified by latitude and longitude (for example: [51.513845, -0.100539]).
        :param gps_accuracy: Accuracy of the GPS coordinates.
        :param battery: Battery level of the device.
        """
        ...

class ffmpeg:

    @staticmethod
    def start(*, entity_id=None):
        """
        Sends a start command to a ffmpeg based sensor.
        :param entity_id: Name of entity that will start. Platform dependent.
        """
        ...

    @staticmethod
    def stop(*, entity_id=None):
        """
        Sends a stop command to a ffmpeg based sensor.
        :param entity_id: Name of entity that will stop. Platform dependent.
        """
        ...

    @staticmethod
    def restart(*, entity_id=None):
        """
        Sends a restart command to a ffmpeg based sensor.
        :param entity_id: Name of entity that will restart. Platform dependent.
        """
        ...

class frontend:

    @staticmethod
    def set_theme(*, name, mode: Literal['', 'dark', 'light']=''):
        """
        Sets the default theme Home Assistant uses. Can be overridden by a user.
        :param name: Name of a theme.
        :param mode: Theme mode.
        """
        ...

    @staticmethod
    def reload_themes():
        """
        Reloads themes from the YAML-configuration.
        """
        ...

class group:

    @staticmethod
    def reload():
        """
        Reloads group configuration, entities, and notify services from YAML-configuration.
        """
        ...

    @staticmethod
    def set(*, object_id: str, name: str='', icon=None, entities=None, add_entities=None, remove_entities=None, all: bool=False):
        """
        Creates/Updates a user group.
        :param object_id: Object ID of this group. This object ID is used as part of the entity ID. Entity ID format: [domain].[object_id].
        :param name: Name of the group.
        :param icon: Name of the icon for the group.
        :param entities: List of all members in the group. Cannot be used in combination with `Add entities` or `Remove entities`.
        :param add_entities: List of members to be added to the group. Cannot be used in combination with `Entities` or `Remove entities`.
        :param remove_entities: List of members to be removed from a group. Cannot be used in combination with `Entities` or `Add entities`.
        :param all: Enable this option if the group should only be used when all entities are in state `on`.
        """
        ...

    @staticmethod
    def remove(*, object_id):
        """
        Removes a group.
        :param object_id: Object ID of this group. This object ID is used as part of the entity ID. Entity ID format: [domain].[object_id].
        """
        ...

class homeassistant:

    @staticmethod
    def save_persistent_states():
        """
        Saves the persistent states immediately. Maintains the normal periodic saving interval.
        """
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """
        Generic action to turn devices off under any domain.
        """
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """
        Generic action to turn devices on under any domain.
        """
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """
        Generic action to toggle devices on/off under any domain.
        """
        ...

    @staticmethod
    def stop():
        """
        Stops Home Assistant.
        """
        ...

    @staticmethod
    def restart():
        """
        Restarts Home Assistant.
        """
        ...

    @staticmethod
    def check_config():
        """
        Checks the Home Assistant YAML-configuration files for errors. Errors will be shown in the Home Assistant logs.
        """
        ...

    @staticmethod
    def update_entity(*, entity_id):
        """
        Forces one or more entities to update its data.
        :param entity_id: List of entities to force update.
        """
        ...

    @staticmethod
    def reload_core_config():
        """
        Reloads the core configuration from the YAML-configuration.
        """
        ...

    @staticmethod
    def set_location(*, latitude: float, longitude: float, elevation: float=0):
        """
        Updates the Home Assistant location.
        :param latitude: Latitude of your location.
        :param longitude: Longitude of your location.
        :param elevation: Elevation of your location.
        """
        ...

    @staticmethod
    def reload_custom_templates():
        """
        Reloads Jinja2 templates found in the `custom_templates` folder in your config. New values will be applied on the next render of the template.
        """
        ...

    @staticmethod
    def reload_config_entry(*, entity_id: str, entry_id: str=''):
        """
        Reloads the specified config entry.
        :param entry_id: The configuration entry ID of the entry to be reloaded.
        """
        ...

    @staticmethod
    def reload_all():
        """
        Reload all YAML configuration that can be reloaded without restarting Home Assistant.
        """
        ...

class image_entity(_entity):
    access_token: Any
    entity_picture: Any
    friendly_name: Any

class image:
    rocky_home = image_entity()

class input_select:

    @staticmethod
    def reload():
        """
        Reloads helpers from the YAML-configuration.
        """
        ...

    @staticmethod
    def select_first(*, entity_id: str):
        """
        Selects the first option.
        """
        ...

    @staticmethod
    def select_last(*, entity_id: str):
        """
        Selects the last option.
        """
        ...

    @staticmethod
    def select_next(*, entity_id: str, cycle: bool=False):
        """
        Select the next option.
        :param cycle: If the option should cycle from the last to the first option on the list.
        """
        ...

    @staticmethod
    def select_option(*, entity_id: str, option: str):
        """
        Selects an option.
        :param option: Option to be selected.
        """
        ...

    @staticmethod
    def select_previous(*, entity_id: str, cycle: bool=False):
        """
        Selects the previous option.
        :param cycle: If the option should cycle from the last to the first option on the list.
        """
        ...

    @staticmethod
    def set_options(*, entity_id: str, options: str):
        """
        Sets the options.
        :param options: List of options.
        """
        ...

class input_button:

    @staticmethod
    def reload():
        """
        Reloads helpers from the YAML-configuration.
        """
        ...

    @staticmethod
    def press(*, entity_id: str):
        """
        Mimics the physical button press on the device.
        """
        ...

class input_number:

    @staticmethod
    def reload():
        """
        Reloads helpers from the YAML-configuration.
        """
        ...

    @staticmethod
    def set_value(*, entity_id: str, value: float):
        """
        Sets the value.
        :param value: The target value.
        """
        ...

    @staticmethod
    def increment(*, entity_id: str):
        """
        Increments the value by 1 step.
        """
        ...

    @staticmethod
    def decrement(*, entity_id: str):
        """
        Decrements the current value by 1 step.
        """
        ...

class input_boolean:

    @staticmethod
    def reload():
        """
        Reloads helpers from the YAML-configuration.
        """
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """
        Turns on the helper.
        """
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """
        Turns off the helper.
        """
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """
        Toggles the helper on/off.
        """
        ...

class input_datetime:

    @staticmethod
    def reload():
        """
        Reloads helpers from the YAML-configuration.
        """
        ...

    @staticmethod
    def set_datetime(*, entity_id: str, date: str='', time: str='', datetime: str='', timestamp: int=0):
        """
        Sets the date and/or time.
        :param date: The target date.
        :param time: The target time.
        :param datetime: The target date & time.
        :param timestamp: The target date & time, expressed by a UNIX timestamp.
        """
        ...

class input_text:

    @staticmethod
    def reload():
        """
        Reloads helpers from the YAML-configuration.
        """
        ...

    @staticmethod
    def set_value(*, entity_id: str, value: str):
        """
        Sets the value.
        :param value: The target value.
        """
        ...

class light_entity(_entity):
    brightness: Any
    color: Any
    color_mode: Any
    color_temp: Any
    color_temp_kelvin: Any
    do_not_disturb: Any
    effect: Any
    effect_list: Any
    entity_id: Any
    friendly_name: Any
    hs_color: Any
    icon: Any
    level_config: Any
    linkquality: Any
    max_color_temp_kelvin: Any
    max_mireds: Any
    min_color_temp_kelvin: Any
    min_mireds: Any
    power_on_behavior: Any
    rgb_color: Any
    supported_color_modes: Any
    supported_features: Any
    update: Any
    update_available: Any
    xy_color: Any

    def turn_on(self, *, transition: int=0, rgb_color=None, kelvin=None, brightness_pct: int=0, brightness_step_pct: int=0, effect: str='', advanced_fields=None):
        """
        Turn on one or more lights and adjust properties of the light, even when they are turned on already.
        :param transition: Duration it takes to get to next state.
        :param rgb_color: The color in RGB format. A list of three integers between 0 and 255 representing the values of red, green, and blue.
        :param kelvin: Color temperature in Kelvin.
        :param brightness_pct: Number indicating the percentage of full brightness, where 0 turns the light off, 1 is the minimum brightness, and 100 is the maximum brightness.
        :param brightness_step_pct: Change brightness by a percentage.
        :param effect: Light effect.
        """
        ...

    def turn_off(self, *, transition: int=0, advanced_fields=None):
        """
        Turn off one or more lights.
        :param transition: Duration it takes to get to next state.
        """
        ...

    def toggle(self, *, transition: int=0, rgb_color=None, kelvin=None, brightness_pct: int=0, effect: str='', advanced_fields=None):
        """
        Toggles one or more lights, from on to off, or, off to on, based on their current state.
        :param transition: Duration it takes to get to next state.
        :param rgb_color: The color in RGB format. A list of three integers between 0 and 255 representing the values of red, green, and blue.
        :param kelvin: Color temperature in Kelvin.
        :param brightness_pct: Number indicating the percentage of full brightness, where 0 turns the light off, 1 is the minimum brightness, and 100 is the maximum brightness.
        :param effect: Light effect.
        """
        ...

class light:
    livingroomlights = light_entity()
    bedroomlights = light_entity()
    corridorlights = light_entity()
    office = light_entity()
    dininglights = light_entity()
    nightstandlights = light_entity()
    filamentlamp = light_entity()
    sofasidetablelight = light_entity()
    centraltablelight = light_entity()
    standinglamp = light_entity()
    wallsidetablelight = light_entity()
    officelight = light_entity()
    bedroomlight = light_entity()
    iris = light_entity()
    sofalight = light_entity()
    wardrobelightsleftcontroller = light_entity()
    wardrobelightsrightcontroller = light_entity()
    corridorlight = light_entity()
    entrancelight = light_entity()
    leftnightstandlight = light_entity()
    rightnightstandlight = light_entity()

    @staticmethod
    def turn_on(*, entity_id: str, transition: int=0, rgb_color=None, kelvin=None, brightness_pct: int=0, brightness_step_pct: int=0, effect: str='', advanced_fields=None):
        """
        Turn on one or more lights and adjust properties of the light, even when they are turned on already.
        :param transition: Duration it takes to get to next state.
        :param rgb_color: The color in RGB format. A list of three integers between 0 and 255 representing the values of red, green, and blue.
        :param kelvin: Color temperature in Kelvin.
        :param brightness_pct: Number indicating the percentage of full brightness, where 0 turns the light off, 1 is the minimum brightness, and 100 is the maximum brightness.
        :param brightness_step_pct: Change brightness by a percentage.
        :param effect: Light effect.
        """
        ...

    @staticmethod
    def turn_off(*, entity_id: str, transition: int=0, advanced_fields=None):
        """
        Turn off one or more lights.
        :param transition: Duration it takes to get to next state.
        """
        ...

    @staticmethod
    def toggle(*, entity_id: str, transition: int=0, rgb_color=None, kelvin=None, brightness_pct: int=0, effect: str='', advanced_fields=None):
        """
        Toggles one or more lights, from on to off, or, off to on, based on their current state.
        :param transition: Duration it takes to get to next state.
        :param rgb_color: The color in RGB format. A list of three integers between 0 and 255 representing the values of red, green, and blue.
        :param kelvin: Color temperature in Kelvin.
        :param brightness_pct: Number indicating the percentage of full brightness, where 0 turns the light off, 1 is the minimum brightness, and 100 is the maximum brightness.
        :param effect: Light effect.
        """
        ...

class logbook:

    @staticmethod
    def log(*, name: str, message: str, entity_id=None, domain: str=''):
        """
        Creates a custom entry in the logbook.
        :param name: Custom name for an entity, can be referenced using an `entity_id`.
        :param message: Message of the logbook entry.
        :param entity_id: Entity to reference in the logbook entry.
        :param domain: Determines which icon is used in the logbook entry. The icon illustrates the integration domain related to this logbook entry.
        """
        ...

class logger:

    @staticmethod
    def set_default_level(*, level: Literal['', 'debug', 'info', 'warning', 'error', 'fatal', 'critical']=''):
        """
        Sets the default log level for integrations.
        :param level: Default severity level for all integrations.
        """
        ...

    @staticmethod
    def set_level():
        """
        Sets the log level for one or more integrations.
        """
        ...

class media_player_entity(_entity):
    adb_response: Any
    app_id: Any
    app_name: Any
    assumed_state: Any
    device_class: Any
    entity_picture_local: Any
    friendly_name: Any
    hdmi_input: Any
    icon: Any
    is_volume_muted: Any
    media_content_type: Any
    media_position_updated_at: Any
    restored: Any
    source_list: Any
    supported_features: Any
    volume_level: Any

    def turn_on(self):
        """
        Turns on the power of the media player.
        """
        ...

    def turn_off(self):
        """
        Turns off the power of the media player.
        """
        ...

    def toggle(self):
        """
        Toggles a media player on/off.
        """
        ...

    def volume_up(self):
        """
        Turns up the volume.
        """
        ...

    def volume_down(self):
        """
        Turns down the volume.
        """
        ...

    def media_play_pause(self):
        """
        Toggles play/pause.
        """
        ...

    def media_play(self):
        """
        Starts playing.
        """
        ...

    def media_pause(self):
        """
        Pauses.
        """
        ...

    def media_stop(self):
        """
        Stops playing.
        """
        ...

    def media_next_track(self):
        """
        Selects the next track.
        """
        ...

    def media_previous_track(self):
        """
        Selects the previous track.
        """
        ...

    def clear_playlist(self):
        """
        Clears the playlist.
        """
        ...

    def volume_set(self, *, volume_level: float):
        """
        Sets the volume level.
        :param volume_level: The volume. 0 is inaudible, 1 is the maximum volume.
        """
        ...

    def volume_mute(self, *, is_volume_muted: bool):
        """
        Mutes or unmutes the media player.
        :param is_volume_muted: Defines whether or not it is muted.
        """
        ...

    def media_seek(self, *, seek_position: float):
        """
        Allows you to go to a different part of the media that is currently playing.
        :param seek_position: Target position in the currently playing media. The format is platform dependent.
        """
        ...

    def join(self, *, group_members):
        """
        Groups media players together for synchronous playback. Only works on supported multiroom audio systems.
        :param group_members: The players which will be synced with the playback specified in `target`.
        """
        ...

    def select_source(self, *, source: str):
        """
        Sends the media player the command to change input source.
        :param source: Name of the source to switch to. Platform dependent.
        """
        ...

    def select_sound_mode(self, *, sound_mode: str=''):
        """
        Selects a specific sound mode.
        :param sound_mode: Name of the sound mode to switch to.
        """
        ...

    def play_media(self, *, media_content_id: str, media_content_type: str, enqueue: Literal['', 'play', 'next', 'add', 'replace']='', announce: bool=False):
        """
        Starts playing specified media.
        :param media_content_id: The ID of the content to play. Platform dependent.
        :param media_content_type: The type of the content to play. Such as image, music, tv show, video, episode, channel, or playlist.
        :param enqueue: If the content should be played now or be added to the queue.
        :param announce: If the media should be played as an announcement.
        """
        ...

    def shuffle_set(self, *, shuffle: bool):
        """
        Playback mode that selects the media in randomized order.
        :param shuffle: Whether or not shuffle mode is enabled.
        """
        ...

    def unjoin(self):
        """
        Removes the player from a group. Only works on platforms which support player groups.
        """
        ...

    def repeat_set(self, *, repeat: Literal['', 'off', 'all', 'one']):
        """
        Playback mode that plays the media in a loop.
        :param repeat: Repeat mode to set.
        """
        ...

class media_player:
    bedroom_tv = media_player_entity()
    sonos = media_player_entity()
    bedroom_tv_2 = media_player_entity()
    fire_tv_192_168_31_201 = media_player_entity()
    lg_webos_smart_tv = media_player_entity()
    googletv9448 = media_player_entity()
    bedroom_gtv = media_player_entity()

    @staticmethod
    def turn_on(*, entity_id: str):
        """
        Turns on the power of the media player.
        """
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """
        Turns off the power of the media player.
        """
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """
        Toggles a media player on/off.
        """
        ...

    @staticmethod
    def volume_up(*, entity_id: str):
        """
        Turns up the volume.
        """
        ...

    @staticmethod
    def volume_down(*, entity_id: str):
        """
        Turns down the volume.
        """
        ...

    @staticmethod
    def media_play_pause(*, entity_id: str):
        """
        Toggles play/pause.
        """
        ...

    @staticmethod
    def media_play(*, entity_id: str):
        """
        Starts playing.
        """
        ...

    @staticmethod
    def media_pause(*, entity_id: str):
        """
        Pauses.
        """
        ...

    @staticmethod
    def media_stop(*, entity_id: str):
        """
        Stops playing.
        """
        ...

    @staticmethod
    def media_next_track(*, entity_id: str):
        """
        Selects the next track.
        """
        ...

    @staticmethod
    def media_previous_track(*, entity_id: str):
        """
        Selects the previous track.
        """
        ...

    @staticmethod
    def clear_playlist(*, entity_id: str):
        """
        Clears the playlist.
        """
        ...

    @staticmethod
    def volume_set(*, entity_id: str, volume_level: float):
        """
        Sets the volume level.
        :param volume_level: The volume. 0 is inaudible, 1 is the maximum volume.
        """
        ...

    @staticmethod
    def volume_mute(*, entity_id: str, is_volume_muted: bool):
        """
        Mutes or unmutes the media player.
        :param is_volume_muted: Defines whether or not it is muted.
        """
        ...

    @staticmethod
    def media_seek(*, entity_id: str, seek_position: float):
        """
        Allows you to go to a different part of the media that is currently playing.
        :param seek_position: Target position in the currently playing media. The format is platform dependent.
        """
        ...

    @staticmethod
    def join(*, entity_id: str, group_members):
        """
        Groups media players together for synchronous playback. Only works on supported multiroom audio systems.
        :param group_members: The players which will be synced with the playback specified in `target`.
        """
        ...

    @staticmethod
    def select_source(*, entity_id: str, source: str):
        """
        Sends the media player the command to change input source.
        :param source: Name of the source to switch to. Platform dependent.
        """
        ...

    @staticmethod
    def select_sound_mode(*, entity_id: str, sound_mode: str=''):
        """
        Selects a specific sound mode.
        :param sound_mode: Name of the sound mode to switch to.
        """
        ...

    @staticmethod
    def play_media(*, entity_id: str, media_content_id: str, media_content_type: str, enqueue: Literal['', 'play', 'next', 'add', 'replace']='', announce: bool=False):
        """
        Starts playing specified media.
        :param media_content_id: The ID of the content to play. Platform dependent.
        :param media_content_type: The type of the content to play. Such as image, music, tv show, video, episode, channel, or playlist.
        :param enqueue: If the content should be played now or be added to the queue.
        :param announce: If the media should be played as an announcement.
        """
        ...

    @staticmethod
    def shuffle_set(*, entity_id: str, shuffle: bool):
        """
        Playback mode that selects the media in randomized order.
        :param shuffle: Whether or not shuffle mode is enabled.
        """
        ...

    @staticmethod
    def unjoin(*, entity_id: str):
        """
        Removes the player from a group. Only works on platforms which support player groups.
        """
        ...

    @staticmethod
    def repeat_set(*, entity_id: str, repeat: Literal['', 'off', 'all', 'one']):
        """
        Playback mode that plays the media in a loop.
        :param repeat: Repeat mode to set.
        """
        ...

class mqtt:

    @staticmethod
    def publish(*, topic: str, payload, evaluate_payload: bool=False, qos: Literal['', '0', '1', '2']='', retain: bool=False):
        """
        Publishes a message to an MQTT topic.
        :param topic: Topic to publish to.
        :param payload: The payload to publish.
        :param evaluate_payload: When `payload` is a Python bytes literal, evaluate the bytes literal and publish the raw data.
        :param qos: Quality of Service to use. 0: At most once. 1: At least once. 2: Exactly once.
        :param retain: If the message should have the retain flag set. If set, the broker stores the most recent message on a topic.
        """
        ...

    @staticmethod
    def dump(*, topic: str='', duration: int=0):
        """
        Writes all messages on a specific topic into the `mqtt_dump.txt` file in your configuration folder.
        :param topic: Topic to listen to.
        :param duration: How long we should listen for messages in seconds.
        """
        ...

    @staticmethod
    def reload():
        """
        Reloads MQTT entities from the YAML-configuration.
        """
        ...

class notify:

    @staticmethod
    def send_message(*, entity_id: str, message: str, title: str=''):
        """
        Sends a notification message.
        :param message: Your notification message.
        :param title: Title for your notification message.
        """
        ...

    @staticmethod
    def persistent_notification(*, message: str, title: str='', data=None):
        """
        Sends a notification that is visible in the notifications panel.
        :param message: Message body of the notification.
        :param title: Title of the notification.
        :param data: Some integrations provide extended functionality. For information on how to use _data_, refer to the integration documentation..
        """
        ...

    @staticmethod
    def mobile_app_12t(*, message: str, title: str='', target=None, data=None):
        """
        Sends a notification message using the mobile_app_12t integration.
        """
        ...

    @staticmethod
    def mobile_app_gt_n8000(*, message: str, title: str='', target=None, data=None):
        """
        Sends a notification message using the mobile_app_gt_n8000 integration.
        """
        ...

    @staticmethod
    def mobile_app_13tpro(*, message: str, title: str='', target=None, data=None):
        """
        Sends a notification message using the mobile_app_13tpro integration.
        """
        ...

    @staticmethod
    def mobile_app_waydroid_spectre(*, message: str, title: str='', target=None, data=None):
        """
        Sends a notification message using the mobile_app_waydroid_spectre integration.
        """
        ...

    @staticmethod
    def mobile_app_pixel_8(*, message: str, title: str='', target=None, data=None):
        """
        Sends a notification message using the mobile_app_pixel_8 integration.
        """
        ...

    @staticmethod
    def mobile_app_redmi(*, message: str, title: str='', target=None, data=None):
        """
        Sends a notification message using the mobile_app_redmi integration.
        """
        ...

    @staticmethod
    def mobile_app_oneplus_watch_2(*, message: str, title: str='', target=None, data=None):
        """
        Sends a notification message using the mobile_app_oneplus_watch_2 integration.
        """
        ...

    @staticmethod
    def mobile_app_xiaomi14(*, message: str, title: str='', target=None, data=None):
        """
        Sends a notification message using the mobile_app_xiaomi14 integration.
        """
        ...

    @staticmethod
    def mobile_app_iphone13(*, message: str, title: str='', target=None, data=None):
        """
        Sends a notification message using the mobile_app_iphone13 integration.
        """
        ...

    @staticmethod
    def notify(*, message: str, title: str='', target=None, data=None):
        """
        Sends a notification message using the notify service.
        """
        ...

    @staticmethod
    def lg_webos_smart_tv(*, message: str, title: str='', target=None, data=None):
        """
        Sends a notification message using the lg_webos_smart_tv service.
        """
        ...

class number_entity(_entity):
    battery: Any
    friendly_name: Any
    icon: Any
    illuminance: Any
    illuminance_lux: Any
    led_indication: Any
    linkquality: Any
    max: Any
    min: Any
    mode: Any
    motion_sensitivity: Any
    occupancy: Any
    occupancy_timeout: Any
    restored: Any
    step: Any
    supported_features: Any
    temperature: Any
    unit_of_measurement: Any

    def set_value(self, *, value: str=''):
        """
        Sets the value of a number.
        :param value: The target value to set.
        """
        ...

class number:
    rocky_volume = number_entity()
    sonos_balance = number_entity()
    sonos_bass = number_entity()
    sonos_treble = number_entity()
    hueentrancesensor_occupancy_timeout = number_entity()
    huecorridorsensor_occupancy_timeout = number_entity()

    @staticmethod
    def set_value(*, entity_id: str, value: str=''):
        """
        Sets the value of a number.
        :param value: The target value to set.
        """
        ...

class persistent_notification:

    @staticmethod
    def create(*, message: str, title: str='', notification_id: str=''):
        """
        Shows a notification on the notifications panel.
        :param message: Message body of the notification.
        :param title: Optional title of the notification.
        :param notification_id: ID of the notification. This new notification will overwrite an existing notification with the same ID.
        """
        ...

    @staticmethod
    def dismiss(*, notification_id: str):
        """
        Removes a notification from the notifications panel.
        :param notification_id: ID of the notification to be removed.
        """
        ...

    @staticmethod
    def dismiss_all():
        """
        Removes all notifications from the notifications panel.
        """
        ...

class person_entity(_entity):
    device_trackers: Any
    editable: Any
    friendly_name: Any
    gps_accuracy: Any
    id: Any
    latitude: Any
    longitude: Any
    source: Any
    user_id: Any

class person:
    jacopo = person_entity()
    zuzanna = person_entity()

    @staticmethod
    def reload():
        """
        Reloads persons from the YAML-configuration.
        """
        ...

class pyscript:

    @staticmethod
    def autocomplete_generator() -> dict[str, Any]:
        """
        https://github.com/dmamelin/pyscript_autocomplete
        """
        ...

    @staticmethod
    def reload(*, global_ctx: str=''):
        """
        Reloads all available pyscripts and restart triggers
        :param global_ctx: Only reload this specific global context (file or app)
        """
        ...

    @staticmethod
    def jupyter_kernel_start(*, key: str, kernel_name: str, shell_port: int=0, iopub_port: int=0, stdin_port: int=0, control_port: int=0, hb_port: int=0, ip: str='', transport: Literal['', 'tcp', 'udp']='', signature_scheme: Literal['', 'hmac-sha256']=''):
        """
        Starts a jupyter kernel for interactive use; Called by Jupyter front end and should generally not be used by users
        :param shell_port: Shell port number
        :param iopub_port: IOPub port number
        :param stdin_port: Stdin port number
        :param control_port: Control port number
        :param hb_port: Heartbeat port number
        :param ip: IP address to connect to Jupyter front end
        :param key: Used for signing
        :param transport: Transport type
        :param signature_scheme: Signing algorithm
        :param kernel_name: Kernel name
        """
        ...

class recorder:

    @staticmethod
    def purge(*, keep_days: int=0, repack: bool=False, apply_filter: bool=False):
        """
        Starts purge task - to clean up old data from your database.
        :param keep_days: Number of days to keep the data in the database. Starting today, counting backward. A value of `7` means that everything older than a week will be purged.
        :param repack: Attempt to save disk space by rewriting the entire database file.
        :param apply_filter: Apply `entity_id` and `event_type` filters in addition to time-based purge.
        """
        ...

    @staticmethod
    def purge_entities(*, entity_id=None, domains=None, entity_globs=None, keep_days: int=0):
        """
        Starts a purge task to remove the data related to specific entities from your database.
        :param entity_id: List of entities for which the data is to be removed from the recorder database.
        :param domains: List of domains for which the data needs to be removed from the recorder database.
        :param entity_globs: List of glob patterns used to select the entities for which the data is to be removed from the recorder database.
        :param keep_days: Number of days to keep the data for rows matching the filter. Starting today, counting backward. A value of `7` means that everything older than a week will be purged. The default of 0 days will remove all matching rows immediately.
        """
        ...

    @staticmethod
    def enable():
        """
        Starts the recording of events and state changes.
        """
        ...

    @staticmethod
    def disable():
        """
        Stops the recording of events and state changes.
        """
        ...

class remote_entity(_entity):
    activity_list: Any
    current_activity: Any
    friendly_name: Any
    supported_features: Any

    def turn_off(self):
        """
        Turns the device off.
        """
        ...

    def turn_on(self, *, activity: str=''):
        """
        Sends the power on command.
        :param activity: Activity ID or activity name to be started.
        """
        ...

    def toggle(self):
        """
        Toggles a device on/off.
        """
        ...

    def send_command(self, *, command, device: str='', num_repeats: int=0, delay_secs: float=0, hold_secs: float=0):
        """
        Sends a command or a list of commands to a device.
        :param device: Device ID to send command to.
        :param command: A single command or a list of commands to send.
        :param num_repeats: The number of times you want to repeat the commands.
        :param delay_secs: The time you want to wait in between repeated commands.
        :param hold_secs: The time you want to have it held before the release is send.
        """
        ...

    def learn_command(self, *, device: str='', command=None, command_type: Literal['', 'ir', 'rf']='', alternative: bool=False, timeout: int=0):
        """
        Learns a command or a list of commands from a device.
        :param device: Device ID to learn command from.
        :param command: A single command or a list of commands to learn.
        :param command_type: The type of command to be learned.
        :param alternative: If code must be stored as an alternative. This is useful for discrete codes. Discrete codes are used for toggles that only perform one function. For example, a code to only turn a device on. If it is on already, sending the code won't change the state.
        :param timeout: Timeout for the command to be learned.
        """
        ...

    def delete_command(self, *, command, device: str=''):
        """
        Deletes a command or a list of commands from the database.
        :param device: Device from which commands will be deleted.
        :param command: The single command or the list of commands to be deleted.
        """
        ...

class remote:
    gtv = remote_entity()
    fire_tv_192_168_31_201 = remote_entity()

    @staticmethod
    def turn_off(*, entity_id: str):
        """
        Turns the device off.
        """
        ...

    @staticmethod
    def turn_on(*, entity_id: str, activity: str=''):
        """
        Sends the power on command.
        :param activity: Activity ID or activity name to be started.
        """
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """
        Toggles a device on/off.
        """
        ...

    @staticmethod
    def send_command(*, entity_id: str, command, device: str='', num_repeats: int=0, delay_secs: float=0, hold_secs: float=0):
        """
        Sends a command or a list of commands to a device.
        :param device: Device ID to send command to.
        :param command: A single command or a list of commands to send.
        :param num_repeats: The number of times you want to repeat the commands.
        :param delay_secs: The time you want to wait in between repeated commands.
        :param hold_secs: The time you want to have it held before the release is send.
        """
        ...

    @staticmethod
    def learn_command(*, entity_id: str, device: str='', command=None, command_type: Literal['', 'ir', 'rf']='', alternative: bool=False, timeout: int=0):
        """
        Learns a command or a list of commands from a device.
        :param device: Device ID to learn command from.
        :param command: A single command or a list of commands to learn.
        :param command_type: The type of command to be learned.
        :param alternative: If code must be stored as an alternative. This is useful for discrete codes. Discrete codes are used for toggles that only perform one function. For example, a code to only turn a device on. If it is on already, sending the code won't change the state.
        :param timeout: Timeout for the command to be learned.
        """
        ...

    @staticmethod
    def delete_command(*, entity_id: str, command, device: str=''):
        """
        Deletes a command or a list of commands from the database.
        :param device: Device from which commands will be deleted.
        :param command: The single command or the list of commands to be deleted.
        """
        ...

class roborock:

    @staticmethod
    def get_maps(*, entity_id: str) -> dict[str, Any]:
        """
        Get the map and room information of your device.
        """
        ...

class scene_entity(_entity):
    entity_id: Any
    friendly_name: Any
    icon: Any
    id: Any

    def delete(self):
        """
        Deletes a dynamically created scene.
        """
        ...

    def turn_on(self, *, transition: int=0):
        """
        Activates a scene.
        :param transition: Time it takes the devices to transition into the states defined in the scene.
        """
        ...

class scene:
    radio = scene_entity()

    @staticmethod
    def reload():
        """
        Reloads the scenes from the YAML-configuration.
        """
        ...

    @staticmethod
    def apply(*, entities, transition: int=0):
        """
        Activates a scene with configuration.
        :param entities: List of entities and their target state.
        :param transition: Time it takes the devices to transition into the states defined in the scene.
        """
        ...

    @staticmethod
    def create(*, scene_id: str, entities=None, snapshot_entities=None):
        """
        Creates a new scene.
        :param scene_id: The entity ID of the new scene.
        :param entities: List of entities and their target state. If your entities are already in the target state right now, use `snapshot_entities` instead.
        :param snapshot_entities: List of entities to be included in the snapshot. By taking a snapshot, you record the current state of those entities. If you do not want to use the current state of all your entities for this scene, you can combine the `snapshot_entities` with `entities`.
        """
        ...

    @staticmethod
    def delete(*, entity_id: str):
        """
        Deletes a dynamically created scene.
        """
        ...

    @staticmethod
    def turn_on(*, entity_id: str, transition: int=0):
        """
        Activates a scene.
        :param transition: Time it takes the devices to transition into the states defined in the scene.
        """
        ...

class schedule:

    @staticmethod
    def reload():
        """
        Reloads schedules from the YAML-configuration.
        """
        ...

class script_entity(_entity):
    current: Any
    friendly_name: Any
    icon: Any
    last_triggered: Any
    max: Any
    mode: Any

    def turn_on(self):
        """
        Runs the sequence of actions defined in a script.
        """
        ...

    def turn_off(self):
        """
        Stops a running script.
        """
        ...

    def toggle(self):
        """
        Toggle a script. Starts it, if isn't running, stops it otherwise.
        """
        ...

class script:
    play_random_media = script_entity()

    @staticmethod
    def play_random_media(*, media_content_ids, media_content_type: str, entity_id, group_members=None, shuffle: bool=False, repeat: Literal['', 'off', 'all', 'one']='', volume_level: float=0) -> dict[str, Any]:
        """
        
        :param media_content_ids: The list of IDs and one will be randomly chosen to play
        :param media_content_type: The type of content that will play. Platform dependent.
        :param entity_id: The entity id that will be used to play and control the specified media.
        :param group_members: The entity ids of the additional entities to group together in a multi-room system. This ignores all types but entity ids.
        :param shuffle: True/false for enabling/disabling shuffle. If not set, current setting is used.
        :param repeat: Repeat mode set to off, all, one. If not set, current mode is used.
        :param volume_level: Float for volume level. Range 0..1. If a value isn't given, volume isn't changed. If you specified Group Members the volume will be applied to all members.
        """
        ...

    @staticmethod
    def reload():
        """
        Reloads all the available scripts.
        """
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """
        Runs the sequence of actions defined in a script.
        """
        ...

    @staticmethod
    def turn_off(*, entity_id: str):
        """
        Stops a running script.
        """
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """
        Toggle a script. Starts it, if isn't running, stops it otherwise.
        """
        ...

class select_entity(_entity):
    battery: Any
    brightness: Any
    color: Any
    color_mode: Any
    color_temp: Any
    friendly_name: Any
    icon: Any
    illuminance: Any
    illuminance_lux: Any
    led_indication: Any
    linkquality: Any
    motion_sensitivity: Any
    occupancy: Any
    occupancy_timeout: Any
    options: Any
    power_on_behavior: Any
    restored: Any
    supported_features: Any
    temperature: Any
    update: Any
    update_available: Any

    def select_first(self):
        """
        Selects the first option.
        """
        ...

    def select_last(self):
        """
        Selects the last option.
        """
        ...

    def select_next(self, *, cycle: bool=False):
        """
        Selects the next option.
        :param cycle: If the option should cycle from the last to the first.
        """
        ...

    def select_option(self, *, option: str):
        """
        Selects an option.
        :param option: Option to be selected.
        """
        ...

    def select_previous(self, *, cycle: bool=False):
        """
        Selects the previous option.
        :param cycle: If the option should cycle from the first to the last.
        """
        ...

class select:
    filamentlamp_power_on_behavior = select_entity()
    table_bulb_power_on_behavior = select_entity()
    sofa_bulb_power_on_behavior = select_entity()
    zigbee2mqtt_bridge_log_level = select_entity()
    zigbee2mqtt_bridge_log_level_2 = select_entity()
    zigbee2mqtt_bridge_log_level_3 = select_entity()
    sofasidetablelight_power_on_behavior = select_entity()
    centraltablelight_power_on_behavior = select_entity()
    standinglamp_power_on_behavior = select_entity()
    wallsidetablelight_power_on_behavior = select_entity()
    officelight_power_on_behavior = select_entity()
    bedroomlight_power_on_behavior = select_entity()
    tuyadial_operation_mode = select_entity()
    rocky_mop_intensity = select_entity()
    rocky_mop_mode = select_entity()
    rocky_selected_map = select_entity()
    iris_power_on_behavior = select_entity()
    hueentrancesensor_motion_sensitivity = select_entity()
    huecorridorsensor_motion_sensitivity = select_entity()
    wardrobelightsleftcontroller_power_on_behavior = select_entity()
    wardrobelightsrightcontroller_power_on_behavior = select_entity()

    @staticmethod
    def select_first(*, entity_id: str):
        """
        Selects the first option.
        """
        ...

    @staticmethod
    def select_last(*, entity_id: str):
        """
        Selects the last option.
        """
        ...

    @staticmethod
    def select_next(*, entity_id: str, cycle: bool=False):
        """
        Selects the next option.
        :param cycle: If the option should cycle from the last to the first.
        """
        ...

    @staticmethod
    def select_option(*, entity_id: str, option: str):
        """
        Selects an option.
        :param option: Option to be selected.
        """
        ...

    @staticmethod
    def select_previous(*, entity_id: str, cycle: bool=False):
        """
        Selects the previous option.
        :param cycle: If the option should cycle from the first to the last.
        """
        ...

class sensor_entity(_entity):
    Available: Any
    Confidence: Any
    Country: Any
    Locality: Any
    Location: Any
    Name: Any
    Ocean: Any
    Thoroughfare: Any
    Total: Any
    Types: Any
    Zones: Any
    action: Any
    action_direction: Any
    action_duration: Any
    action_step_size: Any
    action_time: Any
    action_type: Any
    battery: Any
    brightness: Any
    contact: Any
    device_class: Any
    friendly_name: Any
    humidity: Any
    icon: Any
    illuminance: Any
    illuminance_lux: Any
    led_indication: Any
    linkquality: Any
    motion_sensitivity: Any
    occupancy: Any
    occupancy_timeout: Any
    options: Any
    pm25: Any
    restored: Any
    state_class: Any
    supported_features: Any
    temperature: Any
    unit_of_measurement: Any
    update: Any
    update_available: Any
    voc_index: Any

class sensor:
    sun_next_dawn = sensor_entity()
    sun_next_dusk = sensor_entity()
    sun_next_midnight = sensor_entity()
    sun_next_noon = sensor_entity()
    sun_next_rising = sensor_entity()
    sun_next_setting = sensor_entity()
    gt_n8000_battery_level = sensor_entity()
    gt_n8000_battery_state = sensor_entity()
    gt_n8000_charger_type = sensor_entity()
    zigbee2mqtt_bridge_version = sensor_entity()
    zigbee2mqtt_bridge_permit_join_timeout = sensor_entity()
    arris_tg3492lg_sr_external_ip = sensor_entity()
    arris_tg3492lg_sr_download_speed = sensor_entity()
    arris_tg3492lg_sr_upload_speed = sensor_entity()
    zigbee2mqtt_bridge_version_2 = sensor_entity()
    zigbee2mqtt_bridge_permit_join_timeout_2 = sensor_entity()
    huebutton_battery = sensor_entity()
    huebutton_action = sensor_entity()
    zigbee2mqtt_bridge_version_3 = sensor_entity()
    zigbee2mqtt_bridge_permit_join_timeout_3 = sensor_entity()
    breatherboi_temperature = sensor_entity()
    breatherboi_humidity = sensor_entity()
    breatherboi_pm25 = sensor_entity()
    breatherboi_voc_index = sensor_entity()
    fellerbedroom_action = sensor_entity()
    entranceremote_battery = sensor_entity()
    entranceremote_action_duration = sensor_entity()
    entranceremote_action = sensor_entity()
    officedial_battery = sensor_entity()
    officedial_action = sensor_entity()
    officedial_action_direction = sensor_entity()
    officedial_action_type = sensor_entity()
    officedial_action_time = sensor_entity()
    officedial_brightness = sensor_entity()
    officedial_action_step_size = sensor_entity()
    livingdial_battery = sensor_entity()
    livingdial_action = sensor_entity()
    livingdial_action_direction = sensor_entity()
    livingdial_action_type = sensor_entity()
    livingdial_action_time = sensor_entity()
    livingdial_brightness = sensor_entity()
    livingdial_action_step_size = sensor_entity()
    bedroomdial_battery = sensor_entity()
    bedroomdial_action = sensor_entity()
    bedroomdial_action_direction = sensor_entity()
    bedroomdial_action_type = sensor_entity()
    bedroomdial_action_time = sensor_entity()
    bedroomdial_brightness = sensor_entity()
    bedroomdial_action_step_size = sensor_entity()
    tuyadial_action = sensor_entity()
    tuyadial_action_step_size = sensor_entity()
    tuyadial_action_transition_time = sensor_entity()
    tuyadial_action_rate = sensor_entity()
    tuyadial_battery = sensor_entity()
    innrbutton_action = sensor_entity()
    waydroid_spectre_battery_level = sensor_entity()
    waydroid_spectre_battery_state = sensor_entity()
    waydroid_spectre_charger_type = sensor_entity()
    athom_homelabsmartplug_connected_ssid = sensor_entity()
    athom_homelabsmartplug_current = sensor_entity()
    athom_homelabsmartplug_energy = sensor_entity()
    athom_homelabsmartplug_ip_address = sensor_entity()
    athom_homelabsmartplug_mac_address = sensor_entity()
    athom_homelabsmartplug_power = sensor_entity()
    athom_homelabsmartplug_total_daily_energy = sensor_entity()
    athom_homelabsmartplug_total_energy = sensor_entity()
    athom_homelabsmartplug_uptime_sensor = sensor_entity()
    athom_homelabsmartplug_voltage = sensor_entity()
    athom_homelabsmartplug_wifi_signal = sensor_entity()
    athom_officesmartplug_connected_ssid = sensor_entity()
    athom_officesmartplug_current = sensor_entity()
    athom_officesmartplug_energy = sensor_entity()
    athom_officesmartplug_ip_address = sensor_entity()
    athom_officesmartplug_mac_address = sensor_entity()
    athom_officesmartplug_power = sensor_entity()
    athom_officesmartplug_total_daily_energy = sensor_entity()
    athom_officesmartplug_total_energy = sensor_entity()
    athom_officesmartplug_uptime_sensor = sensor_entity()
    athom_officesmartplug_voltage = sensor_entity()
    athom_officesmartplug_wifi_signal = sensor_entity()
    pixel_8_battery_level = sensor_entity()
    pixel_8_battery_state = sensor_entity()
    pixel_8_charger_type = sensor_entity()
    athom_livingsmartplug_connected_ssid = sensor_entity()
    athom_livingsmartplug_current = sensor_entity()
    athom_livingsmartplug_energy = sensor_entity()
    athom_livingsmartplug_ip_address = sensor_entity()
    athom_livingsmartplug_mac_address = sensor_entity()
    athom_livingsmartplug_power = sensor_entity()
    athom_livingsmartplug_total_daily_energy = sensor_entity()
    athom_livingsmartplug_total_energy = sensor_entity()
    athom_livingsmartplug_uptime_sensor = sensor_entity()
    athom_livingsmartplug_voltage = sensor_entity()
    athom_livingsmartplug_wifi_signal = sensor_entity()
    rocky_main_brush_time_left = sensor_entity()
    rocky_side_brush_time_left = sensor_entity()
    rocky_filter_time_left = sensor_entity()
    rocky_sensor_time_left = sensor_entity()
    rocky_cleaning_time = sensor_entity()
    rocky_total_cleaning_time = sensor_entity()
    rocky_status = sensor_entity()
    rocky_cleaning_area = sensor_entity()
    rocky_total_cleaning_area = sensor_entity()
    rocky_vacuum_error = sensor_entity()
    rocky_battery = sensor_entity()
    rocky_last_clean_begin = sensor_entity()
    rocky_last_clean_end = sensor_entity()
    rocky_cleaning_progress = sensor_entity()
    rocky_dock_error = sensor_entity()
    redmi_battery_level = sensor_entity()
    redmi_battery_state = sensor_entity()
    redmi_charger_type = sensor_entity()
    oneplus_watch_2_battery_level = sensor_entity()
    oneplus_watch_2_battery_state = sensor_entity()
    oneplus_watch_2_charger_type = sensor_entity()
    slzb_06_core_chip_temp = sensor_entity()
    slzb_06_zigbee_chip_temp = sensor_entity()
    frontdoor_battery = sensor_entity()
    xiaomi14_battery_level = sensor_entity()
    xiaomi14_battery_state = sensor_entity()
    xiaomi14_charger_type = sensor_entity()
    iphone_activity = sensor_entity()
    iphone_battery_level = sensor_entity()
    iphone_battery_state = sensor_entity()
    iphone_ssid = sensor_entity()
    iphone_storage = sensor_entity()
    iphone_bssid = sensor_entity()
    iphone_connection_type = sensor_entity()
    iphone_sim_1 = sensor_entity()
    iphone_sim_2 = sensor_entity()
    iphone_geocoded_location = sensor_entity()
    iphone_floors_descended = sensor_entity()
    iphone_distance = sensor_entity()
    iphone_floors_ascended = sensor_entity()
    iphone_last_update_trigger = sensor_entity()
    iphone_app_version = sensor_entity()
    iphone_steps = sensor_entity()
    iphone_average_active_pace = sensor_entity()
    iphone_location_permission = sensor_entity()
    hueentrancesensor_temperature = sensor_entity()
    hueentrancesensor_battery = sensor_entity()
    hueentrancesensor_illuminance_lux = sensor_entity()
    huecorridorsensor_temperature = sensor_entity()
    huecorridorsensor_battery = sensor_entity()
    huecorridorsensor_illuminance_lux = sensor_entity()
    presence_sensor_fp2_56ed_light_sensor_light_level = sensor_entity()
    slzb_06_connection_mode = sensor_entity()
    slzb_06_firmware_channel = sensor_entity()
    slzb_06_zigbee_type = sensor_entity()

class sonos:

    @staticmethod
    def snapshot(*, entity_id=None, with_group: bool=False):
        """
        Takes a snapshot of the media player.
        :param entity_id: Name of entity that will be snapshot.
        :param with_group: True or False. Also snapshot the group layout.
        """
        ...

    @staticmethod
    def restore(*, entity_id=None, with_group: bool=False):
        """
        Restores a snapshot of the media player.
        :param entity_id: Name of entity that will be restored.
        :param with_group: True or False. Also restore the group layout.
        """
        ...

    @staticmethod
    def set_sleep_timer(*, entity_id: str, sleep_time: int=0):
        """
        Sets a Sonos timer.
        :param sleep_time: Number of seconds to set the timer.
        """
        ...

    @staticmethod
    def clear_sleep_timer(*, entity_id: str):
        """
        Clears a Sonos timer.
        """
        ...

    @staticmethod
    def update_alarm(*, entity_id: str, alarm_id: int, time: str='', volume: float=0, enabled: bool=False, include_linked_zones: bool=False):
        """
        Updates an alarm with new time and volume settings.
        :param alarm_id: ID for the alarm to be updated.
        :param time: Set time for the alarm.
        :param volume: Set alarm volume level.
        :param enabled: Enable or disable the alarm.
        :param include_linked_zones: Enable or disable including grouped rooms.
        """
        ...

    @staticmethod
    def play_queue(*, entity_id: str, queue_position: int=0):
        """
        Start playing the queue from the first item.
        :param queue_position: Position of the song in the queue to start playing from.
        """
        ...

    @staticmethod
    def remove_from_queue(*, entity_id: str, queue_position: int=0):
        """
        Removes an item from the queue.
        :param queue_position: Position in the queue to remove.
        """
        ...

    @staticmethod
    def get_queue(*, entity_id: str) -> dict[str, Any]:
        """
        Returns the contents of the queue.
        """
        ...

class switch_entity(_entity):
    battery: Any
    device_class: Any
    friendly_name: Any
    icon: Any
    illuminance: Any
    illuminance_lux: Any
    led_indication: Any
    linkquality: Any
    motion_sensitivity: Any
    occupancy: Any
    occupancy_timeout: Any
    restored: Any
    supported_features: Any
    temperature: Any

    def turn_off(self):
        """
        Turns a switch off.
        """
        ...

    def turn_on(self):
        """
        Turns a switch on.
        """
        ...

    def toggle(self):
        """
        Toggles a switch on/off.
        """
        ...

class switch:
    zigbee2mqtt_bridge_permit_join = switch_entity()
    zigbee2mqtt_bridge_permit_join_2 = switch_entity()
    zigbee2mqtt_bridge_permit_join_3 = switch_entity()
    rocky_child_lock = switch_entity()
    rocky_status_indicator_light = switch_entity()
    rocky_do_not_disturb = switch_entity()
    sonos_crossfade = switch_entity()
    sonos_loudness = switch_entity()
    hueentrancesensor_led_indication = switch_entity()
    huecorridorsensor_led_indication = switch_entity()
    slzb_06_disable_leds = switch_entity()
    slzb_06_led_night_mode = switch_entity()
    slzb_06_auto_zigbee_update = switch_entity()

    @staticmethod
    def turn_off(*, entity_id: str):
        """
        Turns a switch off.
        """
        ...

    @staticmethod
    def turn_on(*, entity_id: str):
        """
        Turns a switch on.
        """
        ...

    @staticmethod
    def toggle(*, entity_id: str):
        """
        Toggles a switch on/off.
        """
        ...

class system_log:

    @staticmethod
    def clear():
        """
        Clears all log entries.
        """
        ...

    @staticmethod
    def write(*, message: str, level: Literal['', 'debug', 'info', 'warning', 'error', 'critical']='', logger: str=''):
        """
        Write log entry.
        :param message: Message to log.
        :param level: Log level.
        :param logger: Logger name under which to log the message. Defaults to `system_log.external`.
        """
        ...

class template:

    @staticmethod
    def reload():
        """
        Reloads template entities from the YAML-configuration.
        """
        ...

class time_entity(_entity):
    friendly_name: Any

    def set_value(self, *, time: str):
        """
        Sets the time.
        :param time: The time to set.
        """
        ...

class time:
    rocky_do_not_disturb_begin = time_entity()
    rocky_do_not_disturb_end = time_entity()

    @staticmethod
    def set_value(*, entity_id: str, time: str):
        """
        Sets the time.
        :param time: The time to set.
        """
        ...

class timer:

    @staticmethod
    def reload():
        """
        Reloads timers from the YAML-configuration.
        """
        ...

    @staticmethod
    def start(*, entity_id: str, duration: str=''):
        """
        Starts a timer.
        :param duration: Duration the timer requires to finish. [optional].
        """
        ...

    @staticmethod
    def pause(*, entity_id: str):
        """
        Pauses a timer.
        """
        ...

    @staticmethod
    def cancel(*, entity_id: str):
        """
        Cancels a timer.
        """
        ...

    @staticmethod
    def finish(*, entity_id: str):
        """
        Finishes a timer.
        """
        ...

    @staticmethod
    def change(*, entity_id: str, duration: str):
        """
        Changes a timer.
        :param duration: Duration to add or subtract to the running timer.
        """
        ...

class tts:

    @staticmethod
    def speak(*, entity_id: str, media_player_entity_id, message: str, cache: bool=False, language: str='', options=None):
        """
        Speaks something using text-to-speech on a media player.
        :param media_player_entity_id: Media players to play the message.
        :param message: The text you want to convert into speech so that you can listen to it on your device.
        :param cache: Stores this message locally so that when the text is requested again, the output can be produced more quickly.
        :param language: Language to use for speech generation.
        :param options: A dictionary containing integration-specific options.
        """
        ...

    @staticmethod
    def clear_cache():
        """
        Removes all cached text-to-speech files and purges the memory.
        """
        ...

    @staticmethod
    def google_translate_say(*, entity_id, message: str, cache: bool=False, language: str='', options=None):
        """
        Say something using text-to-speech on a media player with google_translate.
        """
        ...

    @staticmethod
    def cloud_say(*, entity_id, message: str, cache: bool=False, language: str='', options=None):
        """
        Say something using text-to-speech on a media player with cloud.
        """
        ...

class update_entity(_entity):
    auto_update: Any
    device_class: Any
    entity_picture: Any
    friendly_name: Any
    in_progress: Any
    installed_version: Any
    latest_version: Any
    release_summary: Any
    release_url: Any
    skipped_version: Any
    supported_features: Any
    title: Any

    def install(self, *, version: str='', backup: bool=False):
        """
        Installs an update for this device or service.
        :param version: The version to install. If omitted, the latest version will be installed.
        :param backup: If supported by the integration, this creates a backup before starting the update .
        """
        ...

    def skip(self):
        """
        Marks currently available update as skipped.
        """
        ...

    def clear_skipped(self):
        """
        Removes the skipped version marker from an update.
        """
        ...

class update:
    huebutton = update_entity()
    breatherboi = update_entity()
    sofasidetablelight = update_entity()
    centraltablelight = update_entity()
    standinglamp = update_entity()
    wallsidetablelight = update_entity()
    bedroomlight = update_entity()
    entranceremote = update_entity()
    officedial = update_entity()
    livingdial = update_entity()
    bedroomdial = update_entity()
    hacs_update = update_entity()
    header_authentication_update = update_entity()
    iris = update_entity()
    custom_icon_color_update = update_entity()
    bubble_card_update = update_entity()
    music_assistant_update = update_entity()
    mini_graph_card_update = update_entity()
    browser_mod_update = update_entity()
    button_card_update = update_entity()
    card_mod_update = update_entity()
    mini_media_player_update = update_entity()
    light_entity_card_update = update_entity()
    auto_entities_update = update_entity()
    layout_card_update = update_entity()
    simple_weather_card_update = update_entity()
    state_switch_update = update_entity()
    my_cards_bundle_update = update_entity()
    mushroom_update = update_entity()
    swipe_card_update = update_entity()
    home_assistant_swipe_navigation_update = update_entity()
    frontdoor = update_entity()
    wardrobelightsleftcontroller = update_entity()
    wardrobelightsrightcontroller = update_entity()
    slzb_06_core_firmware = update_entity()
    slzb_06_zigbee_firmware = update_entity()
    pyscript_update = update_entity()

    @staticmethod
    def install(*, entity_id: str, version: str='', backup: bool=False):
        """
        Installs an update for this device or service.
        :param version: The version to install. If omitted, the latest version will be installed.
        :param backup: If supported by the integration, this creates a backup before starting the update .
        """
        ...

    @staticmethod
    def skip(*, entity_id: str):
        """
        Marks currently available update as skipped.
        """
        ...

    @staticmethod
    def clear_skipped(*, entity_id: str):
        """
        Removes the skipped version marker from an update.
        """
        ...

class vacuum_entity(_entity):
    battery_icon: Any
    battery_level: Any
    fan_speed: Any
    fan_speed_list: Any
    friendly_name: Any
    icon: Any
    supported_features: Any

    def start(self):
        """
        Starts or resumes the cleaning task.
        """
        ...

    def pause(self):
        """
        Pauses the cleaning task.
        """
        ...

    def return_to_base(self):
        """
        Tells the vacuum cleaner to return to its dock.
        """
        ...

    def clean_spot(self):
        """
        Tells the vacuum cleaner to do a spot clean-up.
        """
        ...

    def locate(self):
        """
        Locates the vacuum cleaner robot.
        """
        ...

    def stop(self):
        """
        Stops the current cleaning task.
        """
        ...

    def set_fan_speed(self, *, fan_speed: str):
        """
        Sets the fan speed of the vacuum cleaner.
        :param fan_speed: Fan speed. The value depends on the integration. Some integrations have speed steps, like 'medium'. Some use a percentage, between 0 and 100.
        """
        ...

    def send_command(self, *, command: str, params=None):
        """
        Sends a command to the vacuum cleaner.
        :param command: Command to execute. The commands are integration-specific.
        :param params: Parameters for the command. The parameters are integration-specific.
        """
        ...

class vacuum:
    rocky = vacuum_entity()

    @staticmethod
    def start(*, entity_id: str):
        """
        Starts or resumes the cleaning task.
        """
        ...

    @staticmethod
    def pause(*, entity_id: str):
        """
        Pauses the cleaning task.
        """
        ...

    @staticmethod
    def return_to_base(*, entity_id: str):
        """
        Tells the vacuum cleaner to return to its dock.
        """
        ...

    @staticmethod
    def clean_spot(*, entity_id: str):
        """
        Tells the vacuum cleaner to do a spot clean-up.
        """
        ...

    @staticmethod
    def locate(*, entity_id: str):
        """
        Locates the vacuum cleaner robot.
        """
        ...

    @staticmethod
    def stop(*, entity_id: str):
        """
        Stops the current cleaning task.
        """
        ...

    @staticmethod
    def set_fan_speed(*, entity_id: str, fan_speed: str):
        """
        Sets the fan speed of the vacuum cleaner.
        :param fan_speed: Fan speed. The value depends on the integration. Some integrations have speed steps, like 'medium'. Some use a percentage, between 0 and 100.
        """
        ...

    @staticmethod
    def send_command(*, entity_id: str, command: str, params=None):
        """
        Sends a command to the vacuum cleaner.
        :param command: Command to execute. The commands are integration-specific.
        :param params: Parameters for the command. The parameters are integration-specific.
        """
        ...

class weather:

    @staticmethod
    def get_forecasts(*, entity_id: str, type: Literal['', 'daily', 'hourly', 'twice_daily']) -> dict[str, Any]:
        """
        Get weather forecasts.
        :param type: Forecast type: daily, hourly or twice daily.
        """
        ...

class webostv:

    @staticmethod
    def button(*, entity_id, button: str):
        """
        Sends a button press command.
        :param entity_id: Name(s) of the webostv entities where to run the API method.
        :param button: Name of the button to press.  Known possible values are LEFT, RIGHT, DOWN, UP, HOME, MENU, BACK, ENTER, DASH, INFO, ASTERISK, CC, EXIT, MUTE, RED, GREEN, BLUE, YELLOW, VOLUMEUP, VOLUMEDOWN, CHANNELUP, CHANNELDOWN, PLAY, PAUSE, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
        """
        ...

    @staticmethod
    def command(*, entity_id, command: str, payload=None):
        """
        Sends a command.
        :param entity_id: Name(s) of the webostv entities where to run the API method.
        :param command: Endpoint of the command.
        :param payload: An optional payload to provide to the endpoint in the format of key value pair(s).
        """
        ...

    @staticmethod
    def select_sound_output(*, entity_id, sound_output: str):
        """
        Sends the TV the command to change sound output.
        :param entity_id: Name(s) of the webostv entities to change sound output on.
        :param sound_output: Name of the sound output to switch to.
        """
        ...

class zone:

    @staticmethod
    def reload():
        """
        Reloads zones from the YAML-configuration.
        """
        ...