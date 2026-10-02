class MenuNavigator:
    def __init__(self, menu_handler, awake_schedule):
        self._menu_handler = menu_handler
        self._awake_schedule = awake_schedule
        self._menus = {}

    def add_menu(self, name, menu):
        self._menus[name] = menu

    def push_wake_time_modifier(self):
        menu = self._menus['time_modifier']
        self._menu_handler.set_current_menu(menu)
        menu.setup('Wake Time',
                   self._awake_schedule.get_wake_time,
                   self._awake_schedule.set_wake_time)