class MenuNavigator:
    def __init__(self, menu_handler):
        self._menu_handler = menu_handler
        self._menus = {}

    def add_menu(self, name, menu):
        self._menus[name] = menu

    def push_wake_time_modifier(self):
        self._menu_handler.set_current_menu(
            self._menus['time_modifier']
        )