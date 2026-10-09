from pathlib import Path
import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from photo_set_builder.src.data.photo_set_configuration import PhotoSetConfiguration
from photo_set_builder.src.data.photo_set_definition import PhotoSetDefinition
from photo_set_builder.src.photo_set_processing.photo_scanner import PhotoScanner
from photo_set_builder.src.photo_set_processing.photo_set_processor import PhotoSetProcessor
from photo_set_builder.src.photo_set_processing.photo_set_zipper import PhotoSetZipper
from photo_set_builder.src.photo_set_processing.photos_synchroniser import PhotosSynchroniser

class PhotoSetProcessorTests(unittest.TestCase):
    def test_the_photo_set_is_processed_when_include_in_sets_is_true(self):
        self.synchronise_photos_return_value = True

        self.out.process_photo_set(self.photo_set)

        self.assertTrue(self.synchronise_photos_correctly_run)

    def test_the_photo_set_dirty_flag_is_set_when_include_in_sets_is_true_1(self):
        self.synchronise_photos_return_value = True

        self.out.process_photo_set(self.photo_set)

        self.assertTrue(self.photo_set.photo_set_has_changed)

    def test_the_photo_set_dirty_flag_is_set_when_include_in_sets_is_true_2(self):
        self.synchronise_photos_return_value = False

        self.out.process_photo_set(self.photo_set)

        self.assertFalse(self.photo_set.photo_set_has_changed)
        
    def test_the_photo_set_is_not_processed_when_include_in_sets_is_false(self):
        photo_set = PhotoSetDefinition(
            'PhotoSet1',
            Path('path/to/photo_set1'),
            PhotoSetConfiguration(False, 'filter'))
        self.synchronise_photos_correctly_run = False

        self.out.process_photo_set(photo_set)

        self.assertFalse(self.synchronise_photos_correctly_run)
        self.assertFalse(photo_set.photo_set_has_changed)

    def test_if_a_set_is_found_to_be_dirty_it_is_zipped(self):
        self.synchronise_photos_return_value = True

        self.out.process_photo_set(self.photo_set)

        self.photo_set_zipper.zip_photo_set.assert_called_with(
            self.compressed_photos_path
        )

    def test_if_a_set_is_not_found_to_be_dirty_it_is_not_zipped(self):
        self.synchronise_photos_return_value = False

        self.out.process_photo_set(self.photo_set)

        self.photo_set_zipper.zip_photo_set.assert_not_called()

    def setUp(self):
        self.photos_path = Path('path/to/photo_set1')
        self.compressed_photos_path = Path('path/to/photo_set1/compressed')
        self.photo_set = PhotoSetDefinition(
            'PhotoSet1',
            self.photos_path,
            PhotoSetConfiguration(True, 'filter'))
        self.system_operations = Mock(spec=SystemOperations)
        self.photo_scanner = Mock(spec=PhotoScanner)
        self.photo_scanner.scan = self.scan_photos
        self.photos_synchroniser = Mock(spec=PhotosSynchroniser)
        self.photos_synchroniser.synchronise_photos = self.synchronise_photos
        self.photo_set_zipper = Mock(spec=PhotoSetZipper)
        self.out = PhotoSetProcessor(
            self.system_operations,
            self.photo_scanner,
            self.photos_synchroniser,
            self.photo_set_zipper,
            compressed_folder_name='compressed'
            )

    def scan_photos(self, photo_set_path):
        if photo_set_path == self.photos_path:
            return 'list of photos'
        if photo_set_path == self.compressed_photos_path:
            return 'list of compressed photos'

    def synchronise_photos(self, photo_definitions, compressed_photos, compressed_photos_path):
        self.assertEqual(photo_definitions, 'list of photos')
        self.assertEqual(compressed_photos, 'list of compressed photos')
        self.assertEqual(compressed_photos_path, self.compressed_photos_path)
        self.synchronise_photos_correctly_run = True
        return self.synchronise_photos_return_value