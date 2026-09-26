class MenuNavigator:
    def __init__(self,
                 menu_handler,
                 time_modifier_menu):
        self._menu_handler = menu_handler
        self._time_modifier_menu = time_modifier_menu

    def push_wake_time_modifier(self):
        self._menu_handler.set_current_menu(
            self._time_modifier_menu
        )