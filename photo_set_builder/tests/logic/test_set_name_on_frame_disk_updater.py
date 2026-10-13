import unittest

from photo_set_builder.src.logic.set_name_on_frame_disk_updater import SetNameOnFrameDiskUpdater

class SetNameOnFrameDiskUpdaterTests(unittest.TestCase):
    def test_the_name_version_is_incremented(self):
        self.assertEqual(self.out.update_name(
            'name-1'),
            'name-2')
        self.assertEqual(self.out.update_name(
            'name-9'),
            'name-10')

    def test_the_first_version_is_1(self):
        self.assertEqual(self.out.update_name(
            'name'),
            'name-1')

    def setUp(self):
        self.out = SetNameOnFrameDiskUpdater()
