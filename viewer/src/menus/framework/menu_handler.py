from typing import Any

from common.src.system_operations import SystemOperations
from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.photos.historic_photo_chooser import HistoricPhotoChooser

class MenuHandler:
    def __init__(self,
                 system_operations:SystemOperations,
                 historic_photo_chooser:HistoricPhotoChooser):
        self._main_menu = None
        self._system_operations = system_operations
        self._historic_photo_chooser = historic_photo_chooser
        self._current_menu:PhotoFrameMenu | None = None

    def set_main_menu(self, menu:PhotoFrameMenu):
        self._main_menu = menu

    def set_current_menu(self, menu:PhotoFrameMenu|None):
        self._current_menu = menu

        if self._current_menu is None:
            self._historic_photo_chooser.disable()
        else:
            self._historic_photo_chooser.enable()

    def mouse_down(self, x:float, y:float) -> None:
        if self._current_menu is None:
            self.set_current_menu(self._main_menu)
        else:
            self._handle_mouse_down(x,y)

    def render(self, display:Any):
        if self._current_menu is not None:
            self._current_menu.render(display)

    def _handle_mouse_down(self, x:float, y:float):
        assert self._current_menu is not None
        result = self._current_menu.mouse_down(x, y)
        if result == MenuAction.BACK:
            self.set_current_menu(None)

    @property
    def is_image_enabled(self):
        if self._current_menu is not None:
            return self._current_menu.is_image_enabled
        return True
