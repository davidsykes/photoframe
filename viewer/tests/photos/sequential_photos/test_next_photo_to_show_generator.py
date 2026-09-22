import unittest
from unittest.mock import Mock
from viewer.src.photos.photo_history import PhotoHistory
from viewer.src.photos.sequential_photos_new.random_photo_selector import RandomPhotoSelector
from viewer.src.photos.sequential_photos_new.next_photo_to_show_generator import NextPhotoToShowGenerator

class NextPhotoToShowGeneratorTests(unittest.TestCase):
    def test_the_next_selected_photos_are_shown(self):
        self.random_photo_selector.select_photo.side_effect = (
            ['Photo 1', 'Photo 2', 'Photo 3']
        )

        self.assertEqual('Photo 1', self.out.generate_next_photo())
        self.assertEqual('Photo 2', self.out.generate_next_photo())
        self.assertEqual('Photo 3', self.out.generate_next_photo())

    def test_photos_shown_recently_are_skipped(self):
        self.random_photo_selector.select_photo.side_effect = (
            ['Photo 1',
             'Photo 2',
             'Photo 3',
             'Photo 4',
             'Photo 5',
             'Photo 6']
        )
        self.photo_history.has_photo_been_shown_recently.side_effect = [
            False,
            False,
            True,
            False,
            True,
            False,
        ]

        self.assertEqual('Photo 1', self.out.generate_next_photo())
        self.assertEqual('Photo 2', self.out.generate_next_photo())
        self.assertEqual('Photo 4', self.out.generate_next_photo())
        self.assertEqual('Photo 6', self.out.generate_next_photo())

    def test_limit_the_number_of_retried(self):
        self.random_photo_selector.select_photo.return_value = (
            'Repeated Photo'
        )
        self.photo_history.has_photo_been_shown_recently.return_value = (
            True)

        self.assertEqual('Repeated Photo', self.out.generate_next_photo())
        self.assertEqual('Repeated Photo', self.out.generate_next_photo())
        self.assertEqual('Repeated Photo', self.out.generate_next_photo())

    def setUp(self):
        self.random_photo_selector = Mock(spec=RandomPhotoSelector)
        self.photo_history = Mock(spec=PhotoHistory)
        self.photo_history.has_photo_been_shown_recently.return_value = False
        self.out = NextPhotoToShowGenerator(
            self.random_photo_selector,
            self.photo_history,
            10)

