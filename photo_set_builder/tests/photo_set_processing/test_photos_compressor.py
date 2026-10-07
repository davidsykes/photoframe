from pathlib import Path
import unittest
from unittest.mock import Mock, call

from photo_set_builder.src.data.photo_entry import PhotoEntry
from photo_set_builder.src.logic.photo_compressor import PhotoCompressor
from photo_set_builder.src.photo_set_processing.photos_compressor import PhotosCompressor


class PhotosCompressorTests(unittest.TestCase):
    def test_photos_not_compressed_are_compressed(self):
        photos_to_compress = [
            PhotoEntry('image1.jpg', 'image1'),
            PhotoEntry('image2.jpg', 'image2'),
            PhotoEntry('image3.jpg', 'image3'),
            PhotoEntry('image4.jpg', 'image4'),
            PhotoEntry('image5.jpg', 'image5')
        ]

        compressed_photos = {
            'image2': 'compressed_image2.jpg',
            'image4': 'compressed_image4.jpg',
        }

        self.out.compress_photos(photos_to_compress,
                                   compressed_photos,
                                   'compressed_photos_path')

        self.assertEqual(
            self.photo_compressor.compress_photos.call_count, 3
        )
        self.photo_compressor.compress_photos.assert_has_calls(
            [call(photos_to_compress[0], 'compressed_photos_path'),
             call(photos_to_compress[2], 'compressed_photos_path'),
             call(photos_to_compress[4], 'compressed_photos_path'),]
        )

    def setUp(self):
        self.photo_compressor = Mock(spec=PhotoCompressor)
        self.out = PhotosCompressor(
            self.photo_compressor
            )
