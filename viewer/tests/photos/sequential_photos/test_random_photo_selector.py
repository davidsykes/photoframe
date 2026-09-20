import unittest
from unittest.mock import Mock
from viewer.src.photos.random_photo_selection.photo_from_photo_set_selector import PhotoFromPhotoSetSelector
from viewer.src.photos.sequential_photos_new.random_photo_selector_new import RandomPhotoSelectorNew
from viewer.src.photos.sequential_photos_new.random_photo_set_selector import RandomPhotoSetSelector

class RandomPhotoSelectorTests(unittest.TestCase):
    def test_a_random_photo_is_chosen_from_a_random_set(self):
        self.random_photo_set_selector.select_photo_set.return_value = (
            'random set'
        )
        self.photo_from_set_selecter.select_photo.return_value = (
            'random photo'
        )

        photo = self.out.select_photo()

        self.assertEqual(photo, 'random photo')

        self.photo_from_set_selecter.select_photo.assert_called_once_with(
            'random set')


    def setUp(self):
        self.random_photo_set_selector = Mock(spec=RandomPhotoSetSelector)
        self.photo_from_set_selecter = Mock(spec=PhotoFromPhotoSetSelector)
        self.out = RandomPhotoSelectorNew(
            self.random_photo_set_selector,
            self.photo_from_set_selecter)
