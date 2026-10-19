from viewer.src.menus.framework.menu_items.menu_button import MenuButton
from viewer.src.menus.framework.menu_items.menu_button2 import MenuButton2
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class SettingsMenu(PhotoFrameMenu):
    def __init__(self, menu_navigator):
        buttons = [
            MenuButton2(text = 'Set Wake Time',
                       action = self.set_wake_time_action,
                       position = (UIConstants.MENU_MARGIN, 20),
                       size= UIConstants.WIDE_BUTTON_SIZE),
            MenuButton(UIConstants.LONG_BUTTON_LEFT,
                       40,
                       UIConstants.LONG_BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       'Set Sleep Time', self.set_sleep_time_action),
            MenuButton(UIConstants.LONG_BUTTON_LEFT,
                       60,
                       UIConstants.LONG_BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       'Set Image Display Time', self.set_image_display_duration_seconds_action),
            MenuButton(UIConstants.LONG_BUTTON_LEFT,
                       80,
                       UIConstants.LONG_BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       'WiFi', self.wifi)
        ]
        PhotoFrameMenu.__init__(self, buttons, False)

        self._menu_navigator = menu_navigator

    def set_wake_time_action(self):
        self._menu_navigator.push_wake_time_modifier()

    def set_sleep_time_action(self):
        self._menu_navigator.push_sleep_time_modifier()

    def set_image_display_duration_seconds_action(self):
        self._menu_navigator.push_image_display_duration_second_modifier()

    def wifi(self):
        self._menu_navigator.push_wifi_menu()