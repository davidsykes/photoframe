import unittest
from unittest.mock import Mock
from viewer.src.data.photo_set import PhotoSet
from viewer.src.logic.random_monitor import RandomMonitor
from viewer.src.logic.randomiser import Randomiser
from viewer.src.photos.sequential_photos.random_photo_set_selector import RandomPhotoSetSelector

class RandomPhotoSetSelectorTests(unittest.TestCase):
    def test_random_choices_is_called_to_choose_the_set(self):
        self.randomiser.choices.return_value = 1

        result = self.out.select_photo_set()

        self.assertEqual(result, self.set2)

        self.randomiser.choices.assert_called_once_with(
            [0,1,2], [10,20,30])


    def setUp(self):
        self.randomiser = Mock(spec=Randomiser)
        self.set1 = PhotoSet('set 1', 1, 10)
        self.set2 = PhotoSet('set 2', 2, 20)
        self.set3 = PhotoSet('set 3', 3, 30)
        self.sets = [self.set1, self.set2, self.set3]
        self.out = RandomPhotoSetSelector(
            self.randomiser,
            self.sets,
            Mock(spec=RandomMonitor))

