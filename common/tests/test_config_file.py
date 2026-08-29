import unittest

from common.src.config_file import ConfigFile

class TestConfigFile(unittest.TestCase):
    def test_get_returns_correct_value(self):
        self.assertEqual(self.out.get('image_directory'), 'images')

    def test_missing_key(self):
        with self.assertRaises(Exception):
            self.out.get('image_directory2')

    def test_get_or_default_returns_value_if_it_exitsts(self):
        self.assertEqual(
            self.out.get_or_default('image_directory', 'ava'),
            'images')

    def test_get_or_default_returns_default_if_value_does_not_exist(self):
        self.assertEqual(
            self.out.get_or_default('image_directory2', 'ava'),
            'ava')

    def setUp(self):
        self.out = ConfigFile(
            { 'image_directory': 'images' },
            'config name')
