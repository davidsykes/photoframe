from functools import partial

from viewer.src.menus.framework.menu_items.menu_button2 import MenuButton2
from viewer.src.menus.framework.menu_items.menu_text2 import MenuText2
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class WiFiMenu(PhotoFrameMenu):
    def __init__(self,
                 wifi_controller,
                 hotspot_elucidator,
                 wifi):
        self._wifi_controller = wifi_controller
        self._hotspot_elucidator = hotspot_elucidator
        self._status_button = MenuText2('initialising...',
                            (10, 10))
        self._base_buttons = [self._status_button]
        self.add_wifi_buttons(wifi)
        PhotoFrameMenu.__init__(self, self._base_buttons, False)

    def initialise(self):
        hotspots = self._hotspot_elucidator.list_hotspots()
        self._status_button.update_text(hotspots.status)

    def add_wifi_buttons(self, wifi):
        wifis = wifi.split(',') if wifi else []
        y = 20
        for w in wifis:
            self._base_buttons.append(
                MenuButton2(w,
                            partial(self._select_wifi, w),
                            (10, y),
                            UIConstants.SMALL_BUTTON_SIZE)
                            )
            y += UIConstants.SMALL_BUTTON_SIZE[1] + 5

    def _select_wifi(self, wifi):
        print(f'SELELFCLELEL {wifi}')