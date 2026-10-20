from viewer.src.menus.framework.menu_items.menu_button import MenuButton
from viewer.src.menus.framework.menu_items.menu_text2 import MenuText2
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class WiFiMenu(PhotoFrameMenu):
    def __init__(self,
                 wifi_controller,
                 hotspot_elucidator):
        self._wifi_controller = wifi_controller
        self._hotspot_elucidator = hotspot_elucidator
        self._status_button = MenuText2('initialising...',
                            (20, 20))
        buttons = [
            self._status_button,
            MenuButton(UIConstants.LONG_BUTTON_LEFT,
                       20,
                       UIConstants.LONG_BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       'Set Wake Time', self.set_wake_time_action),
            MenuButton(UIConstants.LONG_BUTTON_LEFT,
                       40,
                       UIConstants.LONG_BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       'Set Sleep Time', self.set_sleep_time_action),
            MenuButton(UIConstants.LONG_BUTTON_LEFT,
                       60,
                       UIConstants.LONG_BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       'Set Image Display Time', self.set_image_display_duration_seconds_action)
        ]
        PhotoFrameMenu.__init__(self, buttons, False)

    def set_wake_time_action(self):
        self._menu_navigator.push_wake_time_modifier()

    def set_sleep_time_action(self):
        self._menu_navigator.push_sleep_time_modifier()

    def set_image_display_duration_seconds_action(self):
        self._menu_navigator.push_image_display_duration_second_modifier()

    def initialise(self):
        hotspots = self._hotspot_elucidator.list_hotspots()
        print(f'HOTHOTHOTHOT1 {hotspots}')
        print(f'HOTHOTHOTHOT2 {hotspots.status}')
        self._status_button.update_text(hotspots.status)
