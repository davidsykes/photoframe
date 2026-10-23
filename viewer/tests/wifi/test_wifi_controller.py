import unittest
from unittest.mock import Mock

from common.src.subprocess_wrapper import SubprocessWrapper
from viewer.src.wifi.wifi_controller import WiFiController

class WiFiControllerTests(unittest.TestCase):
    def test_list_hotspots_runs_the_list_hotspot_command(self):
        self.expected_command = ['nmcli', '-t', '-f', 'SSID', 'dev', 'wifi', 'list']
        self.stdout_return = ['a','b']

        hotspots = self.out.list_network_connections()

        self.assertEqual(hotspots,
                         ['a','b'])
        
    def test_delete_runs_the_delete_command(self):
        self.expected_command = ['nmcli',
                                 'connection',
                                 'delete',
                                 '"my ssid"']
        self.stdout_return = 'delete result'

        result = self.out.delete_connection('my ssid')
        
        self.assertEqual(result, 'delete result')
        
    def test_connect_runs_the_connect_command(self):
        self.expected_command = ['nmcli',
                                 'dev',
                                 'wifi',
                                 'connect',
                                 '"my ssid"',
                                 'password',
                                 '"my password"']
        self.stdout_return = 'connection result'

        result = self.out.connect('my ssid', 'my password')
        
        self.assertEqual(result, 'connection result')

    def setUp(self):
        self.subprocess_wrapper = Mock(spec=SubprocessWrapper)
        self.subprocess_wrapper.run_return_stdout = self.run_return_stdout
        self.out = WiFiController(
            self.subprocess_wrapper)

    def run_return_stdout(self, command):
        self.assertEqual(command, self.expected_command)
        return self.stdout_return