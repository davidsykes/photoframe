import unittest
from unittest.mock import Mock, call

from viewer.src.wifi.ssid_connector import SSIDConnector
from viewer.src.wifi.wifi_controller import WiFiController

class SSIDConnectorTests(unittest.TestCase):
    def test_connections_are_deleted_then_attempted(self):
        self.out.connect('my ssid', 'my password')

        self.assertEqual(self.wifi_controller.mock_calls,
                    [
                        call.delete_connection('my ssid'),
                        call.connect('my ssid', 'my password'),
                    ],
                )
        
    def test_the_result_is_returned(self):
        self.wifi_controller.connect.return_value = 'Connection result'

        result = self.out.connect('my ssid', 'my password')

        self.assertEqual(result, 'Connection result')
        
    def test_if_delete_throws_an_exception_the_error_is_returned(self):
        self.wifi_controller.delete_connection.side_effect = Exception("Delete Exception")

        result = self.out.connect('ssid', 'password')
        
        self.assertEqual(result, 'Delete Exception')
        
    def test_if_connect_throws_an_exception_the_error_is_returned(self):
        self.wifi_controller.connect.side_effect = Exception("Connect Exception")

        result = self.out.connect('ssid', 'password')
        
        self.assertEqual(result, 'Connect Exception')

    def setUp(self):
        self.wifi_controller = Mock(spec=WiFiController)
        self.out = SSIDConnector(
            self.wifi_controller)
