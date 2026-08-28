import unittest
from unittest.mock import Mock

from common.src.config_file import ConfigFile
from common.src.config_file_loader import ConfigFileLoader
from common.src.whole_project_configuration import WholeProjectConfiguration


class TestWholeProjectConfiguration(unittest.TestCase):
    def test_load(self):

        self.assertEqual(self.out.remote_config_url, "remote config url")
        self.assertEqual(self.out.images_folder, "images folder")
        self.assertEqual(self.out.sleep_time_seconds, 2)

    def setUp(self):
        data = { "images_folder": "images folder",
                "remote_config_url": "remote config url",
                "sleep_time_seconds": 2,
                "viewer_parameters": "pc" }
        config = ConfigFile(data, 'test config file')
        self.config_file_loader = Mock(spec = ConfigFileLoader)
        self.config_file_loader.load_config_file.return_value = config
        self.out = WholeProjectConfiguration(
            self.config_file_loader
        )
