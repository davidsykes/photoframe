import unittest
from unittest.mock import Mock

from viewer.src.photos.photo_selection.next_photo_selector import NextPhotoSelector
from viewer.src.photos.photo_set_selector import PhotoSetSelector
from viewer.tests.photos.photo_from_photo_set_selector import PhotoFromPhotoSetSelector


class NextImageSelectorTests(unittest.TestCase):
    def test_a_photo_is_selected_from_a_photo_set(self):

        photo = self.out.select_next_photo()

        self.assertEqual(photo, 'selected photo')

    def setUp(self):
        self.photo_set_selector = Mock(spec=PhotoSetSelector)
        self.photo_set_selector.select_photo_set.return_value = 'selected set'
        self.photo_from_photo_set_selector = Mock(
            spec=PhotoFromPhotoSetSelector)
        self.photo_from_photo_set_selector.select_photo = self.mock_select_photo
        self.out = NextPhotoSelector(
            self.photo_set_selector,
            self.photo_from_photo_set_selector)

    def mock_select_photo(self, set):
        if set == 'selected set':
            return 'selected photo'