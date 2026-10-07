from pathlib import Path
import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from photo_set_builder.src.photo_sets_lister import PhotoSetsLister

class PhotoSetsListerTests(unittest.TestCase):
    def test_list_photo_sets_creates_photo_set_defenitions_for_each_folder(self):
        photo_sets = self.out.list_photo_sets(self.images_folder_path)

        self.assertEqual(len(photo_sets), 3)

        self.check_set(photo_sets[0],
                       'photo set 1')
        self.check_set(photo_sets[1],
                       'photo set 2')
        self.check_set(photo_sets[2],
                       'photo set 3')

    def check_set(self, photo_set, name):
        self.assertEqual(photo_set.name, name)
        self.assertEqual(
            photo_set.photo_set_path, self.images_folder_path / name
        )

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.system_operations.list_sub_directories = self.list_sub_directories
        self.out = PhotoSetsLister(self.system_operations)
        self.images_folder_path = Path('test_images_folder')

    def list_sub_directories(self, photo_sets_path):
        self.assertEqual(photo_sets_path, self.images_folder_path)
        return [
            'photo set 1',
            'photo set 2',
            'photo set 3'
        ]
