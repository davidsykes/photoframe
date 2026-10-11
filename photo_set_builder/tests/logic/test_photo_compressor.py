from pathlib import Path
import unittest
from unittest.mock import Mock

from photo_set_builder.src.data.photo_entry import PhotoEntry
from photo_set_builder.src.logic.photo_compressor import PhotoCompressor
from photo_set_builder.src.logic.photo_resizer import PhotoResizer

class PhotoCompressorTests(unittest.TestCase):
    def test_source_and_destination_are_sent_to_the_zipper(self):
        self.out.compress_photo(self.photo, self.compressed_path)

        self.photo_resizer.resize_photo.assert_called_once_with(
            self.source_path, self.destination_path
        )

    def setUp(self):
        self.source_path = 'source path'
        self.compressed_path = Path('compressed path')
        self.photo_name = 'photo name'
        self.destination_path = self.compressed_path / self.photo_name
        self.photo = PhotoEntry(
            self.source_path,
            self.photo_name
        )
        self.photo_resizer = Mock(spec=PhotoResizer)
        self.out = PhotoCompressor(self.photo_resizer)
