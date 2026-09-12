import unittest
from unittest.mock import Mock

from viewer.src.data.photo_set import PhotoSet
from viewer.src.photos.photo_selection.photo_set_selector import PhotoSetSelector
from viewer.src.photos.photo_selection.randomiser import Randomiser

class TestPhotoSetSelector(unittest.TestCase):
    def test_random_choices_is_called_to_choose_the_set(self):
        set1 = PhotoSet(1, 10)
        set2 = PhotoSet(2, 20)
        set3 = PhotoSet(3, 30)
        sets = [set1,set2,set3]

        randomiser = Mock(spec=Randomiser)
        randomiser.choices.return_value = 1

        selector = PhotoSetSelector(randomiser, sets)

        result = selector.select_photo_set()

        self.assertEqual(result, set2)

        randomiser.choices.assert_called_once_with(
            [0,1,2], [10,20,30])


