import unittest
from unittest.mock import Mock

from viewer.src.wifi.hotspot_elucidator import HotSpotElucidator
from viewer.src.wifi.wifi_controller import WiFiController

class HotSpotElucidatorTests(unittest.TestCase):
    def test_list_hotspots_returns_a_list_of_the_hotspits(self):
        self.wifi_controller.list_hotspots.return_value = (
            'la la la'
        )

        hotspots = self.out.list_hotspots()

        self.assertEqual(hotspots,
                         ['a','b'])
        
    def test_if_no_hotspots_are_listed_the_list_is_empty(self):
        self.wifi_controller.list_hotspots.return_value = (
            'la la la'
        )

        hotspots = self.out.list_hotspots()

        self.assertEqual(hotspots,
                         ['a','b'])

    def setUp(self):
        self.wifi_controller = Mock(spec=WiFiController)
        self.out = HotSpotElucidator(
            self.wifi_controller)

    def run_return_stdout(self, command):
        self.assertEqual(command, ['nmcli', 'dev', 'wifi', 'list'])
        return ['a','b']