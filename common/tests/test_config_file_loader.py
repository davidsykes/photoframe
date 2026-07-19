import unittest

from common.src.config_file_loader import ConfigFileLoader

class FileLoader:
    def __init__(self, data):
        self.data = data
    def load_file(self, file_name):
        if file_name == "config.ini":
            return self.data

class TestConfigFileLoader(unittest.TestCase):
    def test_load(self):
        ini_file = self.out.load_config_file("config.ini")

        self.assertEqual(ini_file.get("image_directory"), "images")

    def test_load_failure(self):
        file_loader = FileLoader("invalid json")

        loader = ConfigFileLoader(file_loader)

        with self.assertRaises(Exception) as context:
            loader.load_config_file("config.ini")

    @classmethod
    def setUp(self):
        data = "{ \"image_directory\": \"images\" }"
        file_loader = FileLoader(data)
        self.out = ConfigFileLoader(file_loader)
