import unittest
from unittest.mock import Mock

from viewer.src.photos.photo_selection.photo_set_selector import PhotoSetSelector
from viewer.src.photos.photo_selection.photo_set_selector_non_repeating import PhotoSetSelectorNonRepeating

class PhotoSetSelectorNonRepeatingTests(unittest.TestCase):
    def test_photo_sets_are_selected(self):
        self.photo_set_selector.select_photo_set.side_effect  = (
            ['Set 1', 'Set 2', 'Set 3']
        )

        self.assertEqual(self.out.select_photo_set(),
                         'Set 1')
        self.assertEqual(self.out.select_photo_set(),
                         'Set 2')
        self.assertEqual(self.out.select_photo_set(),
                         'Set 3')

    def test_a_photo_set_is_not_chosen_more_times_than_appropriate(self):
        self.photo_set_selector.select_photo_set.side_effect  = (
            ['Set 1',
             'Set 2', 'Set 2', 'Set 2', 'Set 2', 'Set 2', 'Set 2',
             'Set 3']
        )

        self.assertEqual(self.out.select_photo_set(),
                         'Set 1')
        self.assertEqual(self.out.select_photo_set(),
                         'Set 2')
        self.assertEqual(self.out.select_photo_set(),
                         'Set 2')
        self.assertEqual(self.out.select_photo_set(),
                         'Set 2')
        self.assertEqual(self.out.select_photo_set(),
                         'Set 3')

    def test_the_repeated_checks_have_an_eventual_limit(self):
        self.photo_set_selector.select_photo_set.side_effect  = (
            ['Set 1',
             'Set 2', 'Set 2', 'Set 2', 'Set 2', 'Set 2', 'Set 2',
             'Set 2', 'Set 2', 'Set 2', 'Set 2', 'Set 2', 'Set 2',
             'Set 3']
        )

        self.assertEqual(self.out.select_photo_set(),
                         'Set 1')
        self.assertEqual(self.out.select_photo_set(),
                         'Set 2')
        self.assertEqual(self.out.select_photo_set(),
                         'Set 2')
        self.assertEqual(self.out.select_photo_set(),
                         'Set 2')
        self.assertEqual(self.out.select_photo_set(),
                         'Set 2')
        self.assertEqual(self.out.select_photo_set(),
                         'Set 3')

    def setUp(self):
        self.photo_set_selector = Mock(spec=PhotoSetSelector)
        self.out = PhotoSetSelectorNonRepeating(
            self.photo_set_selector, 3, 10)
