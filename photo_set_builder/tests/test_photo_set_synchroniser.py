from datetime import date
from pathlib import Path
import unittest
from unittest.mock import Mock
from common.src.system_operations import SystemOperations
from photo_set_builder.src.data.photo_set_definition import PhotoSetDefinition
from photo_set_builder.src.data.viewer_config_photo_folder_configuration import ViewerConfigPhotoFolderConfiguration
from photo_set_builder.src.photo_set_synchroniser import PhotoSetSynchroniser
from photo_set_builder.src.viewer_config_manager import ViewerConfigManager

class PhotoSetsSynchroniserTests(unittest.TestCase):
    def test_the_set_zip_file_is_copied_to_dropbox(self):
        self.out.synchronise_photo_set(self.photo_set)

        self.system_operations.shutil_copy.assert_called_once_with(
            Path('zip path'),
            Path('dropbox path/set name.zip')
        )

    def test_if_viewer_config_manager_find_photo_set_config_raises_an_exception_the_zip_file_is_still_copied(self):
        self.viewer_config_manager.find_photo_set_config = Mock()
        self.viewer_config_manager.find_photo_set_config.side_effect = Exception("Test")
        
        with self.assertRaises(Exception):
            self.out.synchronise_photo_set(self.photo_set)

        self.system_operations.shutil_copy.assert_called_once_with(
            Path('zip path'),
            Path('dropbox path/set name.zip')
        )

    def test_if_the_zip_path_has_not_been_set_an_exception_is_thrown(self):
        self.photo_set.zip_path = None

        with self.assertRaises(Exception):
            self.out.synchronise_photo_set(self.photo_set)

    def test_the_local_base_name_is_updated(self):        
        self.out.synchronise_photo_set(self.photo_set)

        self.config_entry.update_version.assert_called()

    def test_the_config_date_is_updated(self):        
        self.out.synchronise_photo_set(self.photo_set)

        self.config_entry.update_date.assert_called_once_with(
            '2042-12-25')

    def setUp(self):
        self.photo_set = PhotoSetDefinition('set name',
                                            'set path',
                                            None,
                                            Path('zip path'))
        self.viewer_config_manager = Mock(ViewerConfigManager)
        self.viewer_config_manager.find_photo_set_config = self.find_photo_set_config
        self.config_entry = Mock(
            spec=ViewerConfigPhotoFolderConfiguration)
        self.system_operations = Mock(spec=SystemOperations)
        self.system_operations.get_today.return_value = date.fromisoformat('2042-12-25')
        self.out = PhotoSetSynchroniser(
            self.system_operations,
            self.viewer_config_manager,
            Path('dropbox path')
            )

    def find_photo_set_config(self, name):
        self.assertEqual(name, 'set name')
        return self.config_entry
