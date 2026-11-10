from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu

class MenuHandler:
    def __init__(self,
                 system_operations):
        self._main_menu = None
        self._system_operations = system_operations
        self._current_menu:PhotoFrameMenu | None = None

    def set_main_menu(self, menu:PhotoFrameMenu):
        self._main_menu = menu

    def set_current_menu(self, menu:PhotoFrameMenu|None):
        if (self._current_menu is not None):
            self._current_menu.on_exit()
        self._current_menu = menu
        if (self._current_menu is not None):
            self._current_menu.on_enter()

    def mouse_down(self, x:float, y:float) -> None:
        if self._current_menu is None:
            self.set_current_menu(self._main_menu)
        else:
            self._handle_mouse_down(x,y)

    def render(self, display):
        if self._current_menu is not None:
            self._current_menu.render(display)

    def _handle_mouse_down(self, x, y):
        result = self._current_menu.mouse_down(x, y)
        if result == MenuAction.BACK:
            self.set_current_menu(None)

    @property
    def is_image_enabled(self):
        if self._current_menu is not None:
            return self._current_menu.is_image_enabled
        return True
