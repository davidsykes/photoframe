import unittest
from unittest.mock import Mock
from common.src.config_file import ConfigFile
from common.src.config_file_loader import ConfigFileLoader
from photo_set_builder.src.logic.json_wrapper import JsonWrapper
from photo_set_builder.src.data.viewer_config_photo_folder_configuration import ViewerConfigPhotoFolderConfiguration
from photo_set_builder.src.viewer_config_manager import ViewerConfigManager

class ViewerConfigManagerTests(unittest.TestCase):
    def test_find_photo_set_config_finds_a_config(self):
        config = self.out.find_photo_set_config('Set 1')
        self.compare_configs(config,
                         ViewerConfigPhotoFolderConfiguration(
                             ['Set 1', '1a', '43 ava', '2026-09-01']))

        config = self.out.find_photo_set_config('Set 3')
        self.assertEqual(config,
                         ViewerConfigPhotoFolderConfiguration(
                             ['Set 3', '3a', '999', 'date']))
        
    def test_find_photo_set_config_finds_a_versioned_config(self):
        config = self.out.find_photo_set_config('Set 2')
        self.assertEqual(config,
                         ViewerConfigPhotoFolderConfiguration(
                             ['Set 2-22', '2a', 'filter', 'date']))

    def test_find_non_existent_photo_set_throws_an_exception(self):
        with self.assertRaises(Exception):
            self.out.find_photo_set_config('set 1')

    def test_photo_set_configuration_versions_can_be_modified(self):
        config = self.out.find_photo_set_config('Set 2')
        config.update_version()
        self.out.mark_as_changed()

        self.out.save_viewer_config_if_changed()

        self.json.dumps.assert_called_once_with(
            self.config_file_path,
            {'version': 31, 'version_list': [['viewer-0.4.6', 'url']], 'photo_folders': [['Set 1', '1a', '43 ava', '2026-09-01'], ['Set 2-23', '2a', 'filter', 'date'], ['Set 3', '3a', '999', 'date']]}
        )

    def test_if_the_config_has_changed_it_is_written_to_file_with_a_new_version(self):
        self.out.mark_as_changed()

        self.out.save_viewer_config_if_changed()

        self.json.dumps.assert_called_once_with(
            self.config_file_path,
            {'version': 31, 'version_list': [['viewer-0.4.6', 'url']], 'photo_folders': [['Set 1', '1a', '43 ava', '2026-09-01'], ['Set 2-22', '2a', 'filter', 'date'], ['Set 3', '3a', '999', 'date']]}
        )

    def test_if_the_config_has_not_changed_it_is_not_written(self):
        self.out.save_viewer_config_if_changed()

        self.json.dumps.assert_not_called()

    def setUp(self):
        self.config_file_loader = Mock(spec=ConfigFileLoader)
        self.config_file_path = 'config file path'
        self.config = ConfigFile(
            {
                'version': '30',
                'version_list':
                [
                    [ 'viewer-0.4.6', 'url'],
                    ],
                    'photo_folders':
                    [
                        [ 'Set 1', '1a', '43 ava', '2026-09-01'],
                        [ 'Set 2-22', '2a', 'filter', 'date'],
                        [ 'Set 3', '3a', '999', 'date'],
                        ]
                        },
                        self.config_file_path
                        )
        self.config_file_loader.load_config_file = self.load_config_file
        self.json = Mock(spec=JsonWrapper)
        self.out = ViewerConfigManager(
            self.config_file_loader,
            self.config_file_path,
            self.json
            )

    def load_config_file(self, config_file_path):
        self.assertEqual(config_file_path, 'config file path')
        return self.config

    def compare_configs(self, one, two):
        self.assertEqual(one.name, two.name)