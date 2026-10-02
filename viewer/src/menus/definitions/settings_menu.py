from viewer.src.menus.framework.menu_items.menu_button import MenuButton
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class SettingsMenu(PhotoFrameMenu):
    def __init__(self, menu_navigator):
        buttons = [
            MenuButton(UIConstants.LONG_BUTTON_LEFT,
                       20,
                       UIConstants.LONG_BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       'Set Wake Time', self.set_wake_time_action),
            MenuButton(UIConstants.LONG_BUTTON_LEFT,
                       30,
                       UIConstants.LONG_BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       'Set Sleep Time', self.set_sleep_time_action)
        ]
        PhotoFrameMenu.__init__(self, buttons, False)

        self._menu_navigator = menu_navigator

    def set_wake_time_action(self):
        self._menu_navigator.push_wake_time_modifier()

    def set_sleep_time_action(self):
        self._menu_navigator.push_sleep_time_modifier()