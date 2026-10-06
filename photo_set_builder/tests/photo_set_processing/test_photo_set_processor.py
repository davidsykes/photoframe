from pathlib import Path
import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from photo_set_builder.src.photo_set_processing.photo_scanner import PhotoScanner
from photo_set_builder.src.photo_set_processing.photo_set_processor import PhotoSetProcessor
from photo_set_builder.src.photo_set_processing.photos_synchroniser import PhotosSynchroniser

class PhotoSetProcessorTests(unittest.TestCase):
    def test_the_photo_set_is_processed(self):
        self.out.process_photo_set(self.photo_set)

        self.assertEqual(
            self.synchronisation_result,
            'processed'
        )

    def setUp(self):
        self.photo_set = Mock(name='PhotoSet1', path=Path('path/to/photo_set1'))
        self.system_operations = Mock(spec=SystemOperations)
        self.photo_scanner = Mock(spec=PhotoScanner)
        self.photo_scanner.scan = self.scan_photos
        self.photos_synchroniser = Mock(spec=PhotosSynchroniser)
        self.photos_synchroniser.synchronise_photos = self.synchronise_photos
        self.out = PhotoSetProcessor(
            self.system_operations,
            self.photo_scanner,
            self.photos_synchroniser,
            compressed_folder_name='compressed'
            )

    def scan_photos(self, photo_set_path):
        if photo_set_path == Path('path/to/photo_set1'):
            #self.assertEqual(photo_set_path, Path('path/to/photo_set1'))
            return 'list of photos'
        if photo_set_path == Path('path/to/photo_set1/compressed'):
            return 'list of compressed photos'

    def synchronise_photos(self, photo_definitions, compressed_photos, compressed_photos_path):
        self.assertEqual(photo_definitions, 'list of photos')
        self.assertEqual(compressed_photos, 'list of compressed photos')
        self.assertEqual(compressed_photos_path, Path('path/to/photo_set1/compressed'))
        self.synchronisation_result = 'processed'
        return self.synchronisation_result