import unittest
from unittest.mock import Mock
from viewer.src.display.image_provider import ImageProvider
from viewer.src.photos.loading_photo_sets.image_from_file_loader import ImageFromFileLoader
from viewer.src.photos.photo_to_display_chooser import PhotoToDisplayChooser

class ImageProviderTests(unittest.TestCase):
    def test_none_returns_none(self):
        self.photo_path_provider.choose_photo.return_value = None

        image = self.out.fetch_image()

        self.assertIsNone(image)

    def test_sequential_images_are_loaded(self):
        self.photo_path_provider.choose_photo.side_effect = [
            'photo 1', 'photo 2', 'photo 3', None
        ]
        self.image_from_file_loader.load_image.side_effect = [
            'image 1', 'image 2', 'image 3'
        ]

        self.assertEqual(self.out.fetch_image(), 'image 1')
        self.assertEqual(self.out.fetch_image(), 'image 2')
        self.assertEqual(self.out.fetch_image(), 'image 3')
        self.assertEqual(self.out.fetch_image(), None)

    def test_images_are_cached(self):
        self.photo_path_provider.choose_photo.side_effect = [
            'photo 1', 'photo 1', 'photo 1', None
        ]
        self.image_from_file_loader.load_image.side_effect = [
            'image 1', 'image 2', 'image 3'
        ]

        self.assertEqual(self.out.fetch_image(), 'image 1')
        self.assertEqual(self.out.fetch_image(), 'image 1')
        self.assertEqual(self.out.fetch_image(), 'image 1')
        self.assertEqual(self.out.fetch_image(), None)

    def setUp(self):
        self.photo_path_provider = Mock(spec=PhotoToDisplayChooser)
        self.image_from_file_loader = Mock(spec=ImageFromFileLoader)
        self.out = ImageProvider(
            self.photo_path_provider,
            self.image_from_file_loader)
