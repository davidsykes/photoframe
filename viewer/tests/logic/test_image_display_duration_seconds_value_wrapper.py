import unittest
from unittest.mock import Mock

from viewer.src.database.photo_frame_database import PhotoFrameDatabase
from viewer.src.logic.image_display_duration_seconds_value_wrapper import ImageDisplayDurationSecondsWrapper

class ImageDisplayDurationSecondsWrapperTests(unittest.TestCase):
    def test_the_value_is_taken_from_the_database(self):
        self.database_value = 123

        duration = ImageDisplayDurationSecondsWrapper(
            self.database,
            999
        )

        self.assertEqual(123, duration.get())
        
    def test_the_default_value_is_taken_if_no_database_value_exists(self):
        self.database_value = None

        duration = ImageDisplayDurationSecondsWrapper(
            self.database,
            999
        )

        self.assertEqual(999, duration.get())
        
    def test_the_value_is_written_to_the_database(self):
        self.database_value = None
        duration = ImageDisplayDurationSecondsWrapper(
            self.database,
            999
        )

        duration.set(456)

        self.database.set_setting.assert_called_once_with(
            'image_display_duration_seconds_value',
            456
        )

    def setUp(self):
        self.database = Mock(spec=PhotoFrameDatabase)
        self.database.get_setting = self.get_setting

    def get_setting(self, value_name):
        self.assertEqual(value_name, 'image_display_duration_seconds_value')
        return self.database_value