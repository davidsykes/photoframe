from viewer.src.menus.menu_action import MenuAction


class MenuHandler:
    def __init__(self, display_controller, system_operations):
        self._main_menu = None
        self._display_controller = display_controller
        self._system_operations = system_operations
        self._menu_enabled = False

    def set_menu(self, menu):
        self._main_menu = menu

    def mouse_down(self, x, y):
        self._system_operations.log(f'Mouse Down {x} {y}')
        self._display_controller.display_on()
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

