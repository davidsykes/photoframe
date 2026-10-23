from functools import partial
from viewer.src.menus.framework.menu_items.menu_button2 import MenuButton2
from viewer.src.menus.framework.menu_items.menu_text2 import MenuText2
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class WiFiMenu(PhotoFrameMenu):
    def __init__(self,
                 system_operations,
                 hotspot_elucidator,
                 ssid_connector,
                 wifi):
        self._system_operations = system_operations
        self._hotspot_elucidator = hotspot_elucidator
        self._ssid_connector = ssid_connector
        self._status_text = MenuText2('initialising...', (10, 5))
        self._ssid_text = MenuText2('...', (10, 10))
        self._ssid = ''
        self._password_text = MenuText2('...', (10, 15))
        self._password = ''
        self._base_buttons = [
            self._status_text,
            self._ssid_text,
            self._password_text,
            MenuButton2('Ok', self.ok, (10, 20), UIConstants.SMALL_BUTTON_SIZE)]
        self.add_wifi_buttons(wifi)
        self._status_info = []
        PhotoFrameMenu.__init__(self, self._base_buttons, False)

    def initialise(self):
        self._system_operations.log('Initialising network connections')
        hotspots = self._hotspot_elucidator.list_network_connections()
        self._system_operations.log(f'hotspots status = "{hotspots.status}"')
        self._system_operations.log(f'hotspots connections "{hotspots.networks}"')
        self._status_text.update_text(hotspots.status)
        self.add_networks(hotspots.networks)
        self._ssid = ''
        self._password = ''

    def render(self, display):
        for s in self._status_info:
            display.print_text(s)
        PhotoFrameMenu.render(self, display)

    def add_wifi_buttons(self, wifi):
        wifis = wifi.split(',') if wifi else []
        y = 30
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
        self._password += wifi
        self._password_text.update_text(self._password)

    def add_networks(self, networks):
        x = 50
        y = 20
        buttons = self._base_buttons.copy()
        for network in networks:
            buttons.append(
                MenuButton2(network,
                            partial(self.select_network, network),
                            (x, y),
                            UIConstants.SMALL_BUTTON_SIZE)
                            )
            y += UIConstants.SMALL_BUTTON_SIZE[1] + 2
        PhotoFrameMenu.__init__(self, buttons, self.is_image_enabled)

    def select_network(self, network):
        self._ssid = network
        self._ssid_text.update_text(self._ssid)

    def ok(self):
        self._status_info.append(f'SSID={self._ssid}')
        self._status_info.append(f'PWD={self._password}')
        result = self._ssid_connector.connect(self._ssid, self._password)
        for r in result.splitlines():
            self._status_info.append(r)