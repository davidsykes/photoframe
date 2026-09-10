import unittest
from unittest.mock import Mock

from common.src.config_file import ConfigFile
from common.src.config_file_loader import ConfigFileLoader
from common.src.config_file_updater import ConfigFileUpdater
from viewer.src.data.remote_config_data_loader import RemoteConfigDataLoader

class RemoteConfigDataLoaderTests(unittest.TestCase):
    def test_the_version_and_photos_are_returned(self):
        config_data = self.out.get_config_data()

        self.assertEqual(config_data.version, '1.2.3')
        self.assertEqual(config_data.photo_folders, 'photo set data')
        self.config_file_updater.update_config_file.assert_called_once_with(
            'remote_config_url',
            'local_config.json')
        self.config_file_loader.load_config_file.assert_called_once_with(
            'local_config.json')

    def test_the_status_is_updated(self):
        self.out.get_config_data()

        self.status_updater.update_status.assert_called_once_with(
            'Last Version Check',
            '1.2.3')

    def setUp(self):
        self.config_file_updater = Mock(spec=ConfigFileUpdater)
        self.config_file_loader = Mock(spec=ConfigFileLoader)
        self.config = Mock(spec=ConfigFile)
        self.config_file_loader.load_config_file.return_value = self.config
        self.config.get = self.mock_get
        self.status_updater = Mock()
        self.out = RemoteConfigDataLoader(
            self.config_file_updater,
            self.config_file_loader,
            self.status_updater,
            'remote_config_url',
            'local_config.json')

    def mock_get(self, value):
        if (value == 'version'):
            return '1.2.3'
        if (value == 'photo_folders'):
            return 'photo set data'