import unittest
from unittest.mock import Mock

from viewer.src.wifi.hotspot_elucidator import HotSpotElucidator
from viewer.src.wifi.wifi_controller import WiFiController

class HotSpotElucidatorTests(unittest.TestCase):
    def test_list_hotspots_returns_a_list_of_the_hotspits(self):
        self.wifi_controller.list_network_connections.return_value = (
"""DIRECT-aS-EPSON-XP-3100 Series
a907
a907
Zen Internet - FRITZ!Box GQ
denthrn
BENN-2.4
TNCAPABD697
Zyxel_6CAF

Zyxel_6CAF

ZyXEL_B020
eb03cd
denthrn

W-537A361
"""
        )

        hotspots = self.out.list_network_connections()

        self.assertEqual(hotspots.networks,
                         [
'DIRECT-aS-EPSON-XP-3100 Series',
'a907',
'Zen Internet - FRITZ!Box GQ',
'denthrn',
'BENN-2.4',
'TNCAPABD697',
'Zyxel_6CAF',
'ZyXEL_B020',
'eb03cd',
'W-537A361'
                         ])
        
    def test_if_no_hotspots_are_listed_the_list_is_empty(self):
        self.wifi_controller.list_network_connections.return_value = ''

        hotspots = self.out.list_network_connections()

        self.assertEqual(hotspots.networks,
                         [])
        
    def test_if_no_hotspots_are_listed_the_status_is_set(self):
        self.wifi_controller.list_network_connections.return_value = ''

        hotspots = self.out.list_network_connections()

        self.assertEqual(hotspots.status,
                         'No Wifi Networks found')
        
    def test_if_the_controller_returns_an_error_the_error_is_returned(self):
        self.wifi_controller.list_network_connections.side_effect = Exception("Test")

        hotspots = self.out.list_network_connections()

        self.assertEqual(hotspots.status,
                         'Test')

    def setUp(self):
        self.wifi_controller = Mock(spec=WiFiController)
        self.out = HotSpotElucidator(
            self.wifi_controller)

    def run_return_stdout(self, command):
        self.assertEqual(command, ['nmcli', 'dev', 'wifi', 'list'])
        return ['a','b']