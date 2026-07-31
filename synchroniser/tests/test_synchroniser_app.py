import unittest
from unittest.mock import Mock

from common.src.config_file import ConfigFile
from synchroniser.src.synchroniser_app import SynchroniserApp


class TestSynchroniserApp(unittest.TestCase):
    def test_operation(self):
        self.out.sync()

        self.remote_config_loader.load_config.assert_called_once_with(
            'remote_config_url'
        )
        self.photo_folders_synchroniser.sync_folders.assert_called_once_with(
            'list of photo folders'
        )

    @classmethod
    def setUp(self):
        whole_project_config = ConfigFile({ "remote_config_url": "remote_config_url" }, 'whole project')
        self.remote_config_loader = Mock()
        self.remote_config_loader.load_config.return_value =\
            ConfigFile({ "photo_folders": 'list of photo folders' }, 'test')
        self.photo_folders_synchroniser = Mock()
        self.out = SynchroniserApp(
            whole_project_config,
            self.remote_config_loader,
            self.photo_folders_synchroniser)
