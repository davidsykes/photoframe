import unittest
from unittest.mock import Mock

from common.src.config_file import ConfigFile
from common.src.config_file_loader import ConfigFileLoader
from photo_set_builder.src.logic.photo_set_config_loader import PhotoSetConfigLoader

class PhotoSetConfigLoaderTests(unittest.TestCase):
    def test_a_basic_config_can_be_loaded(self):
        self.config = ConfigFile(
            {
                'include_in_photo_sets': True,
                'filter': 'filter',
            },
            'config file path'
        )

        config = self.out.load_config('config file path')

        self.assertTrue(config.include_in_sets)
        self.assertEqual('filter', config.filter)

    def test_if_the_file_is_missing_an_exception_is_thrown(self):
        with self.assertRaises(Exception):
            self.out.load_config('config file path')

    def test_if_include_in_photo_sets_is_missing_an_exception_is_thrown(self):
        self.config = ConfigFile({'a': 'b',},'config file path'
        )
        with self.assertRaises(Exception):
            self.out.load_config('config file path')

    def test_if_include_in_photo_sets_is_not_a_bool_an_exception_is_thrown(self):
        self.config = ConfigFile(
            {
                'include_in_photo_sets': 'True',
                'filter': 'filter',
            },
            'config file path'
        )

        with self.assertRaises(Exception):
            self.out.load_config('config file path')

    def setUp(self):
        self.config_file_loader = Mock(spec=ConfigFileLoader)
        self.config_file_loader.load_config_file = self.load_config_file
        self.out = PhotoSetConfigLoader(self.config_file_loader)

    def load_config_file(self, config_path):
        self.assertEqual(config_path, 'config file path')
        return self.config