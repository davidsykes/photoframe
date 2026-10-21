from functools import partial

from viewer.src.menus.framework.menu_items.menu_button2 import MenuButton2
from viewer.src.menus.framework.menu_items.menu_text2 import MenuText2
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class WiFiMenu(PhotoFrameMenu):
    def __init__(self,
                 system_operations,
                 wifi_controller,
                 hotspot_elucidator,
                 wifi):
        self._system_operations = system_operations
        self._wifi_controller = wifi_controller
        self._hotspot_elucidator = hotspot_elucidator
        self._status_button = MenuText2('initialising...',
                            (10, 10))
        self._base_buttons = [self._status_button]
        self.add_wifi_buttons(wifi)
        PhotoFrameMenu.__init__(self, self._base_buttons, False)

    def initialise(self):
        self._system_operations.log('Initialising network connections')
        hotspots = self._hotspot_elucidator.list_network_connections()
        self._system_operations.log(f'status = "{hotspots.status}"')
        self._system_operations.log(f'connections "{hotspots.networks}"')
        self._status_button.update_text(hotspots.status)
        self.add_networks(hotspots.networks)

    def add_wifi_buttons(self, wifi):
        wifis = wifi.split(',') if wifi else []
        y = 20
        for w in wifis:
            self._system_operations.log(
                f'add wifi {w}')
            self._base_buttons.append(
                MenuButton2(w,
                            partial(self.select_wifi, w),
                            (10, y),
                            UIConstants.SMALL_BUTTON_SIZE)
                            )
            y += UIConstants.SMALL_BUTTON_SIZE[1] + 5

    def select_wifi(self, wifi):
        print(f'SELELFCLELEL {wifi}')

    def add_networks(self, networks):
        x = 70
        y = 10
        buttons = self._base_buttons.copy()
        for network in networks:
            buttons.append(
                MenuButton2(network,
                            partial(self.select_network, network),
                            (x, y),
                            UIConstants.SMALL_BUTTON_SIZE)
                            )
            y += UIConstants.SMALL_BUTTON_SIZE[1] + 5
        PhotoFrameMenu.__init__(self, buttons, self.is_image_enabled)

    def select_network(self, network):
        print(f'NENRENRNENRE {network}')