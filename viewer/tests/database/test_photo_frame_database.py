from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock

from viewer.src.database.photo_frame_database import PhotoFrameDatabase


class PhotoFrameDatabaseTests(unittest.TestCase):
    def test_initially_settings_are_not_set(self):
        self.assertIsNone(self.out.get_setting('setting1'))

    def test_a_setting_can_be_set(self):
        self.out.set_setting('setting1', 'value1')

        self.assertEqual('value1', self.out.get_setting('setting1'))

    def setUp(self):
        self._temp_dir = tempfile.TemporaryDirectory()

        database_path = (
            Path(self._temp_dir.name) / 'test.db'
        )
        self.out = PhotoFrameDatabase(str(database_path))
        self.out.initialise()

    def tearDown(self):
        self._temp_dir.cleanup()