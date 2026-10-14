import unittest
from unittest.mock import Mock

from common.src.config_file import ConfigFile
from common.src.config_file_loader import ConfigFileLoader
from photo_set_builder.src.viewer_config_manager import ViewerConfigManager

class ViewerConfigManagerTests(unittest.TestCase):
    def test_find_photo_set_config_finds_a_config(self):
        config = self.out.find_photo_set_config('Set 1')
        self.assertEqual(config, ['Set 1', '1a', '43 ava', '2026-09-01'])

        config = self.out.find_photo_set_config('Set 3')
        self.assertEqual(config, ['Set 3', '3a', '999'])

    def test_find_non_existent_photo_set_throws_an_exception(self):
        with self.assertRaises(Exception):
            config = self.out.find_photo_set_config('set 1')

    def setUp(self):
        self.config_file_loader = Mock(spec=ConfigFileLoader)
        self.config = ConfigFile(
            {
                'version': '30',
                'version_list':
                [
                    [ 'viewer-0.4.6', 'url'],
                    ],
                    'photo_folders':
                    [
                        [ 'Set 1', '1a', '43 ava', '2026-09-01'],
                        [ 'Set 2', '2a'],
                        [ 'Set 3', '3a', '999'],
                        ]
                        },
                        'config file path'
                        )
        self.config_file_loader.load_config_file = self.load_config_file
        self.out = ViewerConfigManager(
            self.config_file_loader,
            'config file path'
            )

    def load_config_file(self, config_file_path):
        self.assertEqual(config_file_path, 'config file path')
        return self.config