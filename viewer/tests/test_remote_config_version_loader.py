import unittest
from unittest.mock import Mock

from viewer.src.remote_config_version_loader import RemoteConfigVersionLoader

class NewAppOrNewPhotosDetectorTests(unittest.TestCase):
    def test_the_version_is_returned(self):
        version = self.out.get_version()

        self.assertEqual(version, '1.2.3')
        self.config_file_updater.update_config_file.assert_called_once_with(
            'remote_config_url',
            'local_config.json')
        self.config_file_loader.load_config_file.assert_called_once_with(
            'local_config.json')
        
    def test_the_status_is_updated(self):
        version = self.out.get_version()

        self.assertEqual(version, '1.2.3')
        self.status_updater.update_status.assert_called_once_with(
            'Last Version Check',
            '1.2.3')

    @classmethod
    def setUp(self):
        self.config_file_updater = Mock()
        self.config_file_loader = Mock()
        self.config = Mock()
        self.config_file_loader.load_config_file.return_value = self.config
        self.config.get.return_value = '1.2.3'
        self.status_updater = Mock()
        self.out = RemoteConfigVersionLoader(
            self.config_file_updater,
            self.config_file_loader,
            self.status_updater,
            'remote_config_url',
            'local_config.json')