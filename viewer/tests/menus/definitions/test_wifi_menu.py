import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from viewer.src.data.wifi_networks import WiFiNetworks
from viewer.src.menus.definitions.wifi_menu import WiFiMenu
from viewer.src.wifi.hotspot_elucidator import HotSpotElucidator
from viewer.src.wifi.wifi_controller import WiFiController

class WiFiMenuTests(unittest.TestCase):
    def test_status_menu_item_is_created(self):
        self.assertEqual(self.out._buttons[0]._text, 'initialising...')

    def test_status_and_wifi_items_are_displayed(self):
        self.out.render(self.display)

        self.assertTrue('initialising...' in self.display.rendered_text)
        self.assertTrue('Wifi 1' in self.display.rendered_text)
        self.assertTrue('Wifi 2' in self.display.rendered_text)
        self.assertTrue('Wifi 3' in self.display.rendered_text)

    def test_if_wifi_entries_are_empty_none_are_displayed(self):
        self.out = WiFiMenu(self.system_operations,
                            self.wifi_controller,
                            self.hotspot_elucidator,
                            "")

        self.out.render(self.display)

        self.assertEqual(4, len(self.display.rendered_text))

    def test_when_initialised_connections_are_shown(self):
        self.out.initialise()
        self.out.render(self.display)

        self.assertTrue('Updated Status' in self.display.rendered_text)
        self.assertTrue('Network 1' in self.display.rendered_text)
        self.assertTrue('Network 2' in self.display.rendered_text)
        self.assertTrue('Network 3' in self.display.rendered_text)

    def test_ssid_and_password_start_empty(self):
        self.out.initialise()

        self.assertEqual('', self.out._ssid)
        self.assertEqual('', self.out._password)

    def test_selecting_ssid_entries_selects_an_ssid(self):
        self.out.initialise()
        self.press_button('Network 2')
        self.press_button('Network 1')
        self.press_button('Network 3')
        
        self.assertEqual('Network 3', self.out._ssid)

    def test_selecting_wifi_entries_builds_a_password(self):
        self.out.initialise()
        self.press_button('Wifi 2')
        self.press_button('Wifi 1')
        self.press_button('Wifi 3')
        
        self.assertEqual('Wifi 2Wifi 1Wifi 3', self.out._password)

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.wifi_controller = Mock(spec=WiFiController)
        self.hotspot_elucidator = Mock(spec=HotSpotElucidator)
        self.hotspot_elucidator.list_network_connections.return_value = (
            WiFiNetworks('Updated Status', ['Network 1', 'Network 2', 'Network 3'])
        )
        self.display = Mock()
        self.display.rendered_text = {}
        self.display.draw_text = self.draw_text
        self.display.wrapper.draw_text = self.draw_text2
        self.out = WiFiMenu(self.system_operations,
                            self.wifi_controller,
                            self.hotspot_elucidator,
                            "Wifi 1,Wifi 2,Wifi 3")

    def draw_text(self, text, colour, coordinates):
        self.display.rendered_text[text] = (colour, coordinates)
    def draw_text2(self, text, position):
        self.display.rendered_text[text] = position

    def press_button(self, button):
        for b in self.out._buttons:
            if b._text == button:
                b.press()