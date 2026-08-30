

class MenuHandler:
    def __init__(self, main_menu):
        self._main_menu = main_menu
        self._menu_enabled = False

    def mouse_down(self, x, y):
        result = False
        if self._menu_enabled:
            result = self._main_menu.mouse_down(x, y)
        else:
            self._menu_enabled = True
        return result

    def render(self, display):
        if self._menu_enabled:
            self._main_menu.render(display)