from pathlib import Path
import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from viewer.src.images.photo_set_loader import PhotoSetLoader
from viewer.src.images.random_weighter import RandomWeighter


class PhotoSetLoaderTests(unittest.TestCase):
    def test_the_photo_set_images_are_loaded(self):
        photo_set = self.out.load_photo_set(
            'photo_set_path', 'photo_set_date')

        self.assertEqual(photo_set.images,
                         ['path/image 1',
                          'path/image 2',
                          'path/image 3']
        )

    def test_the_set_weighting_is_calculated(self):
        photo_set = self.out.load_photo_set(
            'photo_set_path', 'photo_set_date')

        self.assertEqual(photo_set.random_weighting, 123)

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.system_operations.list_files_recursive = self.mock_list_files_recursive
        self.random_weighter = Mock(spec=RandomWeighter)
        self.random_weighter.weigh = self.mock_weigh
        self.out = PhotoSetLoader(self.system_operations,
                                  self.random_weighter,
                                  'excluded_extensions')

    def mock_list_files_recursive(self, path, excluded_extensions):
        if path == 'photo_set_path' and excluded_extensions == 'excluded_extensions':
            return ['path/image 1',
                    'path/image 2',
                    'path/image 3']

    def mock_weigh(self, date):
        if date == 'photo_set_date':
            return 123