import unittest

from common.src.config_file_loader import ConfigFileLoader

class MockSystemOperations:
    def __init__(self, data):
        self.data = data
        self.logs = []
    def load_file(self, file_name):
        if file_name == "config.ini":
            return self.data
    def log(self, text):
        self.logs.append(text)


class TestConfigFileLoader(unittest.TestCase):
    def test_load(self):
        ini_file = self.out.load_config_file("config.ini")

        self.assertEqual(ini_file.get("image_directory"), "images")

    def test_if_the_file_does_not_exist_the_error_is_logged(self):
        ini_file = self.out.load_config_file("not config.ini")

        self.assertIsNone(ini_file)
        self.assertEqual(
            self.system_operations.logs,
            ["Unable to open config file: 'not config.ini'"])

    def test_if_the_json_is_invalid_the_error_is_logged(self):
        self.system_operations.data = 'invalid json'

        ini_file = self.out.load_config_file("config.ini")

        self.assertIsNone(ini_file)
        self.assertEqual(
            self.system_operations.logs,
            ["Failed to parse JSON file 'config.ini': Expecting value: line 1 column 1 (char 0)"])

    @classmethod
    def setUp(self):
        data = "{ \"image_directory\": \"images\" }"
        self.system_operations = MockSystemOperations(data)
        self.out = ConfigFileLoader(self.system_operations)
