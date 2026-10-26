from viewer.src.menus.framework.menu_items.menu_button_text import MenuButtonText
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class SettingsMenu(PhotoFrameMenu):
    def __init__(self, menu_navigator):
        buttons = [
            MenuButtonText(text = 'Set Wake Time',
                       action = self.set_wake_time_action,
                       position = (UIConstants.MENU_MARGIN, 20),
                       size= UIConstants.WIDE_BUTTON_SIZE),
            MenuButtonText('Set Sleep Time',
                           action=self.set_sleep_time_action,
                           rect_xywh=(UIConstants.LONG_BUTTON_LEFT,
                                      40,
                                      UIConstants.LONG_BUTTON_WIDTH,
                                      UIConstants.BUTTON_HEIGHT)
                                      ),
            MenuButtonText('Set Image Display Time',
                           action=self.set_image_display_duration_seconds_action,
                           rect_xywh=(UIConstants.LONG_BUTTON_LEFT,
                                      60,
                                      UIConstants.LONG_BUTTON_WIDTH,
                                      UIConstants.BUTTON_HEIGHT)
                                      ),
            MenuButtonText('WiFi',
                           action=self.wifi,
                           rect_xywh=(UIConstants.LONG_BUTTON_LEFT,
                                      80,
                                      UIConstants.LONG_BUTTON_WIDTH,
                                      UIConstants.BUTTON_HEIGHT)
                                      )
        ]
        super().__init__(buttons, False)

        self._menu_navigator = menu_navigator

    def set_wake_time_action(self):
        self._menu_navigator.push_wake_time_modifier()

    def set_sleep_time_action(self):
        self._menu_navigator.push_sleep_time_modifier()

    def set_image_display_duration_seconds_action(self):
        self._menu_navigator.push_image_display_duration_second_modifier()

    def wifi(self):
        self._menu_navigator.push_wifi_menu()