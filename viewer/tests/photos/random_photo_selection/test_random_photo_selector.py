import unittest
from unittest.mock import Mock

from viewer.src.photos.random_photo_selection_old.photo_set_selector import PhotoSetSelector
from viewer.src.photos.random_photo_selection_old.random_photo_selector import RandomPhotoSelector
from viewer.tests.photos.random_photo_selection.test_photo_from_photo_set_selector import PhotoFromPhotoSetSelector


class NextImageSelectorTests(unittest.TestCase):
    def test_a_photo_is_selected_from_a_photo_set(self):

        photo = self.out.select_random_photo()

        self.assertEqual(photo, 'selected photo')

    def setUp(self):
        self.photo_set_selector = Mock(spec=PhotoSetSelector)
        self.photo_set_selector.select_photo_set.return_value = 'selected set'
        self.photo_from_photo_set_selector = Mock(
            spec=PhotoFromPhotoSetSelector)
        self.photo_from_photo_set_selector.select_photo = self.mock_select_photo
        self.out = RandomPhotoSelector(
            self.photo_set_selector,
            self.photo_from_photo_set_selector,
            Mock())

    def mock_select_photo(self, photo_set):
        if photo_set == 'selected set':
            return 'selected photo'