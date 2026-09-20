import unittest
from unittest.mock import Mock

from viewer.src.data.photo_set import PhotoSet
from viewer.src.photos.random_photo_selection.randomiser import Randomiser
from viewer.src.photos.sequential_photos_new.photo_from_photo_set_selector import PhotoFromPhotoSetSelectorNew

class TestPhotoFromPhotoSetSelector(unittest.TestCase):
    def test_random_is_called_to_choose_the_photo(self):
        self.randomiser.random.return_value = 2

        self.assertEqual('Photo 3', self.out.select_photo(self.photo_set))

        self.randomiser.random.assert_called_once_with(4)


    def setUp(self):
        self.randomiser = Mock(spec=Randomiser)
        self.out = PhotoFromPhotoSetSelectorNew(
            self.randomiser)
        self.photo_set = PhotoSet('name', 
            ['Photo 1', 'Photo 2', 'Photo 3', 'Photo 4'], 1)
