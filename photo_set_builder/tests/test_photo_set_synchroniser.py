from datetime import date
import unittest
from unittest.mock import Mock
from common.src.system_operations import SystemOperations
from photo_set_builder.src.data.photo_set_definition import PhotoSetDefinition
from photo_set_builder.src.logic.set_name_on_frame_disk_updater import SetNameOnFrameDiskUpdater
from photo_set_builder.src.photo_set_synchroniser import PhotoSetSynchroniser
from photo_set_builder.src.viewer_config_manager import ViewerConfigManager

class PhotoSetsSynchroniserTests(unittest.TestCase):
    @unittest.skip
    def test_the_set_zip_file_is_copied_to_dropbox(self):
        self.out.synchronise_photo_set(self.photo_set)

        self.system_operations.shutil_copy.assert_called_once_with(
            'set zip path',
            'set dropbox target'
        )

    def test_the_local_base_name_is_updated(self):        
        self.out.synchronise_photo_set(self.photo_set)

        self.assertEqual(
            self.viewer_config_manager.config_entry[0],
            'updated set name on frame disk')

    def test_the_config_date_is_updated(self):        
        self.out.synchronise_photo_set(self.photo_set)

        self.assertEqual(
            self.viewer_config_manager.config_entry[3],
            '2042-12-25')

    def setUp(self):
        self.photo_set = PhotoSetDefinition('set name',
                                            'set path',
                                            None)
        self.viewer_config_manager = Mock(ViewerConfigManager)
        self.viewer_config_manager.find_photo_set_config = self.find_photo_set_config
        self.viewer_config_manager.config_entry = [
            'set name on frame disk',
            'dropbox url',
            'filter',
            'date'
        ]
        self.system_operations = Mock(spec=SystemOperations)
        self.system_operations.get_today.return_value = date.fromisoformat('2042-12-25')
        self.set_name_on_frame_disk_updater = Mock(spec=SetNameOnFrameDiskUpdater)
        self.set_name_on_frame_disk_updater.update_name = self.update_name
        self.out = PhotoSetSynchroniser(
            self.system_operations,
            self.viewer_config_manager,
            self.set_name_on_frame_disk_updater
            )

    def find_photo_set_config(self, name):
        self.assertEqual(name, 'set name')
        return self.viewer_config_manager.config_entry

    def update_name(self, name):
        self.assertEqual(name, 'set name on frame disk')
        return 'updated set name on frame disk'