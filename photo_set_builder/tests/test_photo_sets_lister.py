from pathlib import Path
import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from photo_set_builder.src.photo_sets_lister import PhotoSetsLister

class PhotoSetsListerTests(unittest.TestCase):
    def test_list_photo_sets_creates_photo_sets_for_each_folder(self):
        photo_sets = self.out.list_photo_sets(self.images_folder_path)

        self.assertEqual(len(photo_sets), 3)
        self.assertEqual(
            photo_sets[0].name, 'photo set 1'
        )
        self.assertEqual(
            photo_sets[0].path, self.images_folder_path / 'photo set 1'
        )
        self.assertEqual(
            photo_sets[1].name, 'photo set 2'
        )
        self.assertEqual(
            photo_sets[1].path, self.images_folder_path / 'photo set 2'
        )
        self.assertEqual(
            photo_sets[2].name, 'photo set 3'
        )
        self.assertEqual(
            photo_sets[2].path, self.images_folder_path / 'photo set 3'
        )

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.system_operations.listdir = self.listdir
        self.out = PhotoSetsLister(self.system_operations)
        self.images_folder_path = Path('test_images_folder')

    def listdir(self, photo_sets_path):
        self.assertEqual(photo_sets_path, self.images_folder_path)
        return [
            'photo set 1',
            'photo set 2',
            'photo set 3'
        ]