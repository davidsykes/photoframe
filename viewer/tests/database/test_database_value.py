import unittest
from unittest.mock import Mock

from viewer.src.database.database_value import DatabaseValue
from viewer.src.database.photo_frame_database import PhotoFrameDatabase

class DatabaseValueTests(unittest.TestCase):
    def test_the_value_is_taken_from_the_database(self):
        self.database = Mock(spec=PhotoFrameDatabase)
        self.database.get_setting.return_value = '123'
        self.out = DatabaseValue(self.database,
                                 'value name',
                                 60)

        self.database.get_setting.assert_called_once_with('value name')
        self.assertEqual(
            self.out.get_int(),
            123)            

    def test_if_no_value_is_stored_the_default_value_is_taken(self):
        self.database = Mock(spec=PhotoFrameDatabase)
        self.database.get_setting.return_value = None
        self.out = DatabaseValue(self.database,
                                 'value name',
                                 60)

        self.database.get_setting.assert_called_once_with('value name')
        self.assertEqual(
            self.out.get_int(),
            60)
