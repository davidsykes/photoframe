import unittest
from unittest.mock import Mock

from viewer.src.photos.photo_selection.photo_from_photo_set_selector import PhotoFromPhotoSetSelector
from viewer.src.photos.photo_selection.photo_from_photo_set_selector_non_repeating import PhotoFromPhotoSetSelectorNonRepeating


class TestPhotoFromPhotoSetSelectorNonRepeating(unittest.TestCase):
    def test_the_photo_from_photo_set_selector_is_used(self):
        self.photo_from_photo_set_selector.select_photo.side_effect = (
            [1,2,3,4]
        )

        self.assertEqual(1, self.out.select_photo('photo_set'))
        self.assertEqual(2, self.out.select_photo('photo_set'))
        self.assertEqual(3, self.out.select_photo('photo_set'))
        self.assertEqual(4, self.out.select_photo('photo_set'))

        self.photo_from_photo_set_selector.select_photo.assert_called_with('photo_set')

    def test_a_photo_is_not_repeated_within_n_photos(self):
        self.photo_from_photo_set_selector.select_photo.side_effect = (
            [1,2,3,2,4,2,5,2,6,2,7]
        )

        self.assertEqual(1, self.out.select_photo('photo_set'))
        self.assertEqual(2, self.out.select_photo('photo_set'))
        self.assertEqual(3, self.out.select_photo('photo_set'))
        self.assertEqual(4, self.out.select_photo('photo_set'))
        self.assertEqual(5, self.out.select_photo('photo_set'))
        self.assertEqual(6, self.out.select_photo('photo_set'))
        self.assertEqual(2, self.out.select_photo('photo_set'))
        self.assertEqual(7, self.out.select_photo('photo_set'))

    def test_infinitely_repeating_images_does_not_cause_an_infinite_loop(self):
        self.photo_from_photo_set_selector.select_photo.side_effect = (
            [1,2,2,2,2,2,2,2,2,2,2,2,2]
        )

        self.assertEqual(1, self.out.select_photo('photo_set'))
        self.assertEqual(2, self.out.select_photo('photo_set'))
        self.assertEqual(2, self.out.select_photo('photo_set'))

    def setUp(self):
        self.photo_from_photo_set_selector = Mock(spec=PhotoFromPhotoSetSelector)
        self.out = PhotoFromPhotoSetSelectorNonRepeating(
            self.photo_from_photo_set_selector, 4, 6)
