class MenuNavigator:
    def __init__(self,
                 menu_handler,
                 awake_schedule,
                 image_display_duration_value):
        self._menu_handler = menu_handler
        self._awake_schedule = awake_schedule
        self._image_display_duration_value = image_display_duration_value
        self._menus = {}

    def add_menu(self, name, menu):
        self._menus[name] = menu

    def push_wake_time_modifier(self):
        menu = self._menus['time_modifier']
        self._menu_handler.set_current_menu(menu)
        menu.setup('Wake Time',
                   self._awake_schedule.get_wake_time,
                   self._awake_schedule.set_wake_time)

    def push_sleep_time_modifier(self):
        menu = self._menus['time_modifier']
        self._menu_handler.set_current_menu(menu)
        menu.setup('Sleep Time',
                   self._awake_schedule.get_sleep_time,
                   self._awake_schedule.set_sleep_time)

    def push_image_display_duration_second_modifier(self):
        menu = self._menus['value_modifier']
        self._menu_handler.set_current_menu(menu)
        menu.setup('Image Display Time',
                   self._image_display_duration_value.get,
                   self._image_display_duration_value.set)

    def push_wifi_menu(self):
        menu = self._menus['wifi_menu']
        self._menu_handler.set_current_menu(menu)
        menu.initialise()