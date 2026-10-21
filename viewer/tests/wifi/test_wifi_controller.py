import unittest
from unittest.mock import Mock

from common.src.subprocess_wrapper import SubprocessWrapper
from viewer.src.wifi.wifi_controller import WiFiController

class WiFiControllerTests(unittest.TestCase):
    def test_list_hotspots_runs_the_list_hotspot_command(self):
        hotspots = self.out.list_network_connections()

        self.assertEqual(hotspots,
                         ['a','b'])

    def setUp(self):
        self.subprocess_wrapper = Mock(spec=SubprocessWrapper)
        self.subprocess_wrapper.run_return_stdout = self.run_return_stdout
        self.out = WiFiController(
            self.subprocess_wrapper)

    def run_return_stdout(self, command):
        self.assertEqual(command,
                         ['nmcli', '-t', '-f', 'SSID', 'dev', 'wifi', 'list'])
        return ['a','b']