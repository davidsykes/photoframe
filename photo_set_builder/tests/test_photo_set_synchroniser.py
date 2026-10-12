from datetime import date
from pathlib import Path
import unittest
from unittest.mock import Mock
from common.src.system_operations import SystemOperations
from photo_set_builder.src.data.photo_set_definition import PhotoSetDefinition
from photo_set_builder.src.logic.set_name_on_frame_disk_updater import SetNameOnFrameDiskUpdater
from photo_set_builder.src.photo_set_synchroniser import PhotoSetSynchroniser
from photo_set_builder.src.viewer_config_manager import ViewerConfigManager

class PhotoSetsSynchroniserTests(unittest.TestCase):
    def test_the_set_zip_file_is_copied_to_dropbox(self):
        self.out.synchronise_photo_set(self.photo_set)

        self.system_operations.shutil_copy.assert_called_once_with(
            Path('zip path'),
            Path('dropbox path/set name.zip')
        )

    def test_if_the_set_zip_has_not_been_set_an_exception_is_thrown(self):
        self.photo_set.zip_path = None

        with self.assertRaises(Exception):
            self.out.synchronise_photo_set(self.photo_set)

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
                                            None,
                                            Path('zip path'))
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
            self.set_name_on_frame_disk_updater,
            Path('dropbox path')
            )

    def find_photo_set_config(self, name):
        self.assertEqual(name, 'set name')
        return self.viewer_config_manager.config_entry

    def update_name(self, name):
        self.assertEqual(name, 'set name on frame disk')
        return 'updated set name on frame disk'