from viewer.src.menus.menu_action import MenuAction


class MenuHandler:
    def __init__(self, main_menu):
        self._main_menu = main_menu
        self._menu_enabled = False

    def mouse_down(self, x, y):
        if self._menu_enabled:
            self.handle_mouse_down(x,y)
        else:
            self._menu_enabled = True

    def render(self, display):
        if self._menu_enabled:
            self._main_menu.render(display)

    def handle_mouse_down(self, x, y):
        result = self._main_menu.mouse_down(x, y)
        if result == MenuAction.BACK:
            self._menu_enabled = False

