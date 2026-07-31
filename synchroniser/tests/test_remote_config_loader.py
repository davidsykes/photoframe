from pathlib import Path
import unittest
from unittest.mock import Mock

from synchroniser.src.remote_config_loader import RemoteConfigLoader


class TestRemoteConfigLoader(unittest.TestCase):
    def test_operation(self):
        config = self.out.load_config(self.remote_config_url)

        self.config_file_updater.update_config_file.assert_called_once_with(
            self.remote_config_url,
            Path('working_folder') / 'local_config_name.json'
        )
        self.config_file_loader.load_config_file.assert_called_once_with(
            Path('working_folder') / 'local_config_name.json'
        )

        self.assertEqual(config, self.loaded_config)

    @classmethod
    def setUp(self):
        self.remote_config_url = 'remote_config_url'
        self.working_folder = 'working_folder'
        self.local_config_name = 'local_config_name'
        self.config_file_updater = Mock()
        self.loaded_config = 'loaded_config'
        self.config_file_loader = Mock()
        self.config_file_loader.load_config_file.return_value = self.loaded_config
        self.out = RemoteConfigLoader(
            self.working_folder,
            self.local_config_name,
            self.config_file_updater,
            self.config_file_loader
        )
