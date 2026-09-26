from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.menu_button import MenuButton
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class FirstMenu(PhotoFrameMenu):
    def __init__(self,
                 menu_handler,
                 settings_menu,
                 debug_menu,
                 historic_photo_chooser):
        buttons = [
            MenuButton(UIConstants.BUTTON_LEFT , 47, UIConstants.BUTTON_WIDTH, UIConstants.BUTTON_HEIGHT, 'Previous', self.previous_image),
            MenuButton(UIConstants.BUTTON_RIGHT, 47, UIConstants.BUTTON_WIDTH, UIConstants.BUTTON_HEIGHT, 'Next', self.next_image),
            MenuButton(UIConstants.BUTTON_LEFT , 90, UIConstants.BUTTON_WIDTH, UIConstants.BUTTON_HEIGHT, 'Debug', self.debug_menu),
            MenuButton(UIConstants.BUTTON_RIGHT, 90, UIConstants.BUTTON_WIDTH, UIConstants.BUTTON_HEIGHT, 'Settings', self.settings_menu),
        ]
        PhotoFrameMenu.__init__(self, buttons, True)

        self._menu_handler = menu_handler
        self._settings_menu = settings_menu
        self._debug_menu = debug_menu
        self._historic_photo_chooser = historic_photo_chooser
        self._debug_menu_enabled = False

    def on_enter(self):
        self._historic_photo_chooser.enable()

    def on_exit(self):
        self._historic_photo_chooser.disable()

    def render(self, display):
        PhotoFrameMenu.render(self, display)
        if self._debug_menu_enabled:
            self._debug_menu.render(display)

    def mouse_down(self, x, y):
        self.menu_action = PhotoFrameMenu.mouse_down(self, x, y)
        if self._debug_menu_enabled:
            return self._debug_menu.mouse_down(x, y)
        return self.menu_action

    def previous_image(self):
        self._historic_photo_chooser.back()

    def next_image(self):
        self._historic_photo_chooser.forward()

    def debug_menu(self):
        #self._menu_handler.set_current_menu(self._debug_menu)
        self._debug_menu_enabled = not self._debug_menu_enabled

    def settings_menu(self):
        self._menu_handler.set_current_menu(self._settings_menu)