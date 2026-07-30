import unittest
from unittest.mock import Mock

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
        remote_config_url = { "remote_config_url": "remote_config_url" }
        self.remote_config_loader = Mock()
        self.remote_config_loader.load_config.return_value =\
            { "photo_folders": 'list of photo folders' }
        self.photo_folders_synchroniser = Mock()
        self.out = SynchroniserApp(
            remote_config_url,
            self.remote_config_loader,
            self.photo_folders_synchroniser)
