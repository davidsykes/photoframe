from viewer.src.menus.framework.menu_items.menu_button_image import MenuButtonImage
from viewer.src.menus.framework.menu_items.menu_button_text import MenuButtonText
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class SettingsMenu(PhotoFrameMenu):
    def __init__(self, menu_navigator, debug_menu):
        buttons = [
            MenuButtonImage('Set Wake Time',
                            'viewer/src/data/sunrise.jpg',
                            self.set_wake_time_action,
                            position=(UIConstants.MENU_MARGIN + 10,
                                      UIConstants.MENU_MARGIN + 10),
                                      size = UIConstants.MENU_IMAGE_SIZE2),
            MenuButtonImage('Set Wake Time',
                            'viewer/src/data/moonlight.jpg',
                            self.set_sleep_time_action,
                            position=(UIConstants.MENU_MARGIN + 40,
                                      UIConstants.MENU_MARGIN + 10),
                                      size = UIConstants.MENU_IMAGE_SIZE2),
            MenuButtonImage('Set Image Display Time',
                            'viewer/src/data/image_timer.png',
                            self.set_image_display_duration_seconds_action,
                            position=(UIConstants.MENU_MARGIN + 10,
                                      UIConstants.MENU_MARGIN + 40),
                                      size = UIConstants.MENU_IMAGE_SIZE2),
            MenuButtonImage('WiFi',
                            'viewer/src/data/wifi.png',
                            self.wifi,
                            position=(UIConstants.SCREEN_WIDTH - UIConstants.MENU_MARGIN -UIConstants.MENU_IMAGE_SIZE[0],
                                      UIConstants.SCREEN_HEIGHT - UIConstants.MENU_MARGIN - UIConstants.MENU_IMAGE_SIZE[1]),
                            size = UIConstants.MENU_IMAGE_SIZE),
            MenuButtonImage('Debug',
                            'viewer/src/data/debug.png',
                            self.debug,
                            position=(UIConstants.MENU_MARGIN,
                                      UIConstants.SCREEN_HEIGHT - UIConstants.MENU_MARGIN - UIConstants.MENU_IMAGE_SIZE[1]),
                            size = UIConstants.MENU_IMAGE_SIZE),
        ]
        super().__init__(buttons, False)

        self._menu_navigator = menu_navigator
        self._debug_menu = debug_menu
        self._debug_menu_enabled = False

    def render(self, display):
        PhotoFrameMenu.render(self, display)
        if self._debug_menu_enabled:
            self._debug_menu.render(display)

    def set_wake_time_action(self):
        self._menu_navigator.push_wake_time_modifier()

    def set_sleep_time_action(self):
        self._menu_navigator.push_sleep_time_modifier()

    def set_image_display_duration_seconds_action(self):
        self._menu_navigator.push_image_display_duration_second_modifier()

    def wifi(self):
        self._menu_navigator.push_wifi_menu()

    def debug(self):
        self._debug_menu_enabled = not self._debug_menu_enabled
