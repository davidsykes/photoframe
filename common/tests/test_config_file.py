import unittest

from common.src.config_file import ConfigFile

class TestConfigFile(unittest.TestCase):
    def test_get_returns_correct_value(self):
        self.assertEqual(self.out.get("image_directory"), "images")

    def test_missing_key(self):
        with self.assertRaises(Exception) as context:
            self.out.get("image_directory2")

    @classmethod
    def setUp(self):
        self.out = ConfigFile(
            { "image_directory": "images" },
            "config name")
