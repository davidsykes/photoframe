import unittest
from unittest.mock import Mock

from common.src.config_file import ConfigFile
from common.src.config_file_loader import ConfigFileLoader
from common.src.whole_project_configuration import WholeProjectConfiguration


class TestWholeProjectConfiguration(unittest.TestCase):
    def test_basic_load(self):
        data = { "images_folder": "images folder",
                "remote_config_url": "remote config url",
                "image_display_seconds": 2,
                "photo_set_filter": 'filter',
                "viewer_parameters": "pc",
                 "hide_mouse": False }
        config = self.set_up_config(data)
        self.assertEqual(config.remote_config_url, "remote config url")
        self.assertEqual(config.images_folder, "images folder")
        self.assertEqual(config.image_display_seconds, 2)
        self.assertEqual(config.photo_set_filter, 'filter')
        self.assertEqual(config.hide_mouse, False)

    def test_basic_load_old_version(self):
        data = { "images_folder": "images folder",
                "remote_config_url": "remote config url",
                "sleep_time_seconds": 2 }
        config = self.set_up_config(data)
        self.assertEqual(config.remote_config_url, "remote config url")
        self.assertEqual(config.images_folder, "images folder")
        self.assertEqual(config.image_display_seconds, 2)
        self.assertEqual(config.photo_set_filter, 'ava')
        self.assertEqual(config.hide_mouse, True)

    def test_the_filter_defaults_to_ava(self):
        config = self.set_up_config(self.minimal_data)

        self.assertEqual(config.photo_set_filter, 'ava')

    def test_hide_mouse_defaults_to_true(self):
        config = self.set_up_config(self.minimal_data)

        self.assertEqual(config.hide_mouse, True)

    def test_wake_time_defaults_to_1000(self):
        config = self.set_up_config(self.minimal_data)

        self.assertEqual(config.wake_time, "10:00")

    def test_sleep_time_defaults_to_2000(self):
        config = self.set_up_config(self.minimal_data)

        self.assertEqual(config.sleep_time, "20:00")

    def setUp(self):
        self.minimal_data = { "images_folder": "images folder",
                "remote_config_url": "remote config url",
                "image_display_seconds": 2,
                "viewer_parameters": "pc" }

    def set_up_config(self, data):
        config = ConfigFile(data, 'test config file')
        config_file_loader = Mock(spec = ConfigFileLoader)
        config_file_loader.load_config_file.return_value = config
        return WholeProjectConfiguration(
            config_file_loader
        )
