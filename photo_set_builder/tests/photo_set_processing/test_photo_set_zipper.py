from pathlib import Path
import unittest
from unittest.mock import Mock

from photo_set_builder.src.photo_set_processing.photo_set_zipper import PhotoSetZipper
from photo_set_builder.src.zipper.zipper_implementation import ZipperImplementation

class PhotoSetZipperTests(unittest.TestCase):
    def test_the_zipper_implemantaion_is_called(self):
        self.out.zip_photo_set('set name', 'files path')

        self.zipper_implementation.zip.assert_called_once_with(
            'set name',
            'files path'
        )

    def setUp(self):
        self.zipper_implementation = Mock(spec=ZipperImplementation)
        self.out = PhotoSetZipper(self.zipper_implementation)
