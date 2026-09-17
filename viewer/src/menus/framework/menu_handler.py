from viewer.src.menus.framework.menu_action import MenuAction

class MenuHandler:
    def __init__(self,
                 display_on_off_controller,
                 system_operations):
        self._main_menu = None
        self._display_on_off_controller = display_on_off_controller
        self._system_operations = system_operations
        self._current_menu = None

    def set_main_menu(self, menu):
        self._main_menu = menu

    def set_current_menu(self, menu):
        self._current_menu = menu

    def mouse_down(self, x, y):
        self._system_operations.log(f'Mouse Down {x} {y}')
        self._display_on_off_controller.display_on()
        if self._current_menu is None:
            self._current_menu = self._main_menu
        else:
            self.handle_mouse_down(x,y)

    def render(self, display):
        pass
        if self._current_menu is not None:
            self._current_menu.render(display)

    def handle_mouse_down(self, x, y):
        result = self._current_menu.mouse_down(x, y)
        if result == MenuAction.BACK:
            self._current_menu = None
