import unittest
from unittest.mock import Mock

from photo_set_builder.src.logic.list_to_dict_converter import ListToDictConverter
from photo_set_builder.src.photo_set_processing.compressed_photos_remover import CompressedPhotosRemover
from photo_set_builder.src.photo_set_processing.photos_compressor import PhotosCompressor
from photo_set_builder.src.photo_set_processing.photos_synchroniser import PhotosSynchroniser


class PhotosSynchroniserTests(unittest.TestCase):
    def test_photos_and_compressed_index_is_passed_to_the_compresser(self):
        self.out.synchronise_photos(self.photos,
                                    self.compressed_photos,
                                    self.compressed_photos_path)

        self.photo_compressor.compress_photos.assert_called_once_with(
            self.photos,
            self.compressed_photos_dictionary,
            self.compressed_photos_path
        )

    def test_the_compressed_photos_remover_is_called(self):
        self.out.synchronise_photos(self.photos,
                                    self.compressed_photos,
                                    self.compressed_photos_path)

        self.compressed_photos_remover.remove_compressed_photos.assert_called_once_with(
            self.compressed_photos,
            self.photos_dictionary,
            self.compressed_photos_path
        )

    def test_the_synchroniser_ors_the_return_values(self):
        self.check_result(False, False, False)
        self.check_result(True, False, True)
        self.check_result(False, True, True)
        self.check_result(True, True, True)

    def check_result(self, a, b, c):
        self.photo_compressor.compress_photos.return_value = a
        self.compressed_photos_remover.remove_compressed_photos.return_value = b
        self.assertEqual(c,
                         self.out.synchronise_photos(
                             self.photos,
                             self.compressed_photos,
                             self.compressed_photos_path))

    def setUp(self):
        self.photos = 'photos'
        self.photos_dictionary = 'photos_dictionary'
        self.compressed_photos = 'compressed_photos'
        self.compressed_photos_dictionary = 'compressed_photos_dictionary'
        self.compressed_photos_path = 'compressed_photos_path'
        self.list_to_dict_converter = Mock(spec=ListToDictConverter)
        self.list_to_dict_converter.convert = self.convert_list_to_dict
        self.photo_compressor = Mock(spec=PhotosCompressor)
        self.compressed_photos_remover = Mock(spec=CompressedPhotosRemover)
        self.out = PhotosSynchroniser(
            self.list_to_dict_converter,
            self.photo_compressor,
            self.compressed_photos_remover
        )

    def convert_list_to_dict(self, list_to_convert):
        return list_to_convert + '_dictionary'