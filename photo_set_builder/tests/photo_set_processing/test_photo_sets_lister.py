from pathlib import Path
import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from photo_set_builder.src.data.photo_set_configuration import PhotoSetConfiguration
from photo_set_builder.src.logic.photo_set_config_loader import PhotoSetConfigLoader
from photo_set_builder.src.photo_set_processing.photo_sets_lister import PhotoSetsLister

class PhotoSetsListerTests(unittest.TestCase):
    def test_list_photo_sets_creates_photo_set_defenitions_for_each_folder(self):
        photo_sets = self.out.list_photo_sets(self.images_folder_path)

        self.assertEqual(len(photo_sets), 3)

        self.check_set(photo_sets[0],
                       'photo set 1',
                       self.photo_set_configs[0])
        self.check_set(photo_sets[1],
                       'photo set 2',
                       self.photo_set_configs[1])
        self.check_set(photo_sets[2],
                       'photo set 3',
                       self.photo_set_configs[2])

    def check_set(self, photo_set, name, config):
        self.assertEqual(photo_set.name, name)
        self.assertEqual(
            photo_set.photo_set_path, self.images_folder_path / name
        )
        self.assertEqual(photo_set.config, config)

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.system_operations.list_sub_directories = self.list_sub_directories
        self.photo_set_config_loader = Mock(spec=PhotoSetConfigLoader)
        self.photo_set_config_loader.load_config = self.load_photo_set_config
        self.out = PhotoSetsLister(self.system_operations,
                                   self.photo_set_config_loader)
        self.images_folder_path = Path('test_images_folder')
        self.photo_set_configs = [
            PhotoSetConfiguration(True, 'a'),
            PhotoSetConfiguration(False, 'b'),
            PhotoSetConfiguration(True, 'c')
        ]

    def list_sub_directories(self, photo_sets_path):
        self.assertEqual(photo_sets_path, self.images_folder_path)
        return [
            'photo set 1',
            'photo set 2',
            'photo set 3'
        ]

    def load_photo_set_config(self, config_path):
        if config_path == Path('test_images_folder/photo set 1/config.json'):
            return self.photo_set_configs[0]
        if config_path == Path('test_images_folder/photo set 2/config.json'):
            return self.photo_set_configs[1]
        if config_path == Path('test_images_folder/photo set 3/config.json'):
            return self.photo_set_configs[2]
