import sys
sys.path.append('common/src')
import unittest
from ini_file_loader import IniFileLoader

class FileLoader:
    def __init__(self, data):
        self.data = data
    def load_file(self, file_name):
        if file_name == "config.ini":
            return self.data

class TestGetReturnsAString(unittest.TestCase):
    def test_load(self):
        data = "{ \"image_directory\": \"images\" }"
        file_loader = FileLoader(data)

        ini_file = IniFileLoader(file_loader, "config.ini")

        self.assertEqual(ini_file.get("image_directory"), "images")

class TestGettingAMissingValueThrowsAnException(unittest.TestCase):
    def test_load(self):
        data = "{ \"image_directory\": \"images\" }"
        file_loader = FileLoader(data)

        ini_file = IniFileLoader(file_loader, "config.ini")

        with self.assertRaises(Exception) as context:
            ini_file.get("image_directory2")

if __name__ == "__main__":
    unittest.main()