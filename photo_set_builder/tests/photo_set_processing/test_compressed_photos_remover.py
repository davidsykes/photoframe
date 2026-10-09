from pathlib import Path
import unittest
from unittest.mock import Mock, call

from common.src.system_operations import SystemOperations
from photo_set_builder.src.data.photo_entry import PhotoEntry
from photo_set_builder.src.photo_set_processing.compressed_photos_remover import CompressedPhotosRemover

class CompressedPhotosRemoverTests(unittest.TestCase):
    def test_compressed_photos_with_no_original_are_removed(self):
        compressed_photos = [
            PhotoEntry('image1.jpg', 'image1'),
            PhotoEntry('image2.jpg', 'image2'),
            PhotoEntry('image3.jpg', 'image3'),
            PhotoEntry('image4.jpg', 'image4'),
            PhotoEntry('image5.jpg', 'image5')
        ]

        photos_dictionary = {
            'image2': 'compressed_image2.jpg',
            'image4': 'compressed_image4.jpg',
        }

        self.out.remove_compressed_photos(
            compressed_photos,
            photos_dictionary,
            self.compressed_photos_path)

        self.assertEqual(
            self.system_operations.log.call_count, 3
        )
        self.system_operations.log.assert_has_calls(
            [call('Delete compressed file compressed_photos_path\\image1'),
             call('Delete compressed file compressed_photos_path\\image3'),
             call('Delete compressed file compressed_photos_path\\image5')]

        # self.assertEqual(
        #     self.system_operations.delete_file.call_count, 3
        # )
        # self.system_operations.delete_file.assert_has_calls(
        #     [call(self.compressed_photos_path / 'image1'),
        #      call(self.compressed_photos_path / 'image3'),
        #      call(self.compressed_photos_path / 'image5')]
        )
    
    def test_if_photos_are_removed_true_is_returned(self):
        compressed_photos = [
            PhotoEntry('image1.jpg', 'image1'),
            PhotoEntry('image2.jpg', 'image2'),
            PhotoEntry('image3.jpg', 'image3'),
            PhotoEntry('image4.jpg', 'image4'),
            PhotoEntry('image5.jpg', 'image5')
        ]

        photos_dictionary = {
            'image2': 'compressed_image2.jpg',
            'image4': 'compressed_image4.jpg',
        }

        result = self.out.remove_compressed_photos(
            compressed_photos,
            photos_dictionary,
            self.compressed_photos_path)

        self.assertTrue(result)
    
    def test_if_no_photos_are_removed_false_is_returned(self):
        compressed_photos = [
            PhotoEntry('image2.jpg', 'image2'),
            PhotoEntry('image4.jpg', 'image4'),
        ]

        photos_dictionary = {
            'image2': 'compressed_image2.jpg',
            'image4': 'compressed_image4.jpg',
        }

        result = self.out.remove_compressed_photos(
            compressed_photos,
            photos_dictionary,
            self.compressed_photos_path)

        self.assertFalse(result)

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.compressed_photos_path = Path('compressed_photos_path')
        self.out = CompressedPhotosRemover(
            self.system_operations
            )
