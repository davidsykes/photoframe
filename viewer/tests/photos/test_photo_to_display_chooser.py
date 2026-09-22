import unittest
from unittest.mock import Mock

from viewer.src.awake_periods.awake_decider import AwakeDecider
from viewer.src.photos.historic_photo_chooser import HistoricPhotoChooser
from viewer.src.photos.photo_to_display_chooser import PhotoToDisplayChooser
from viewer.src.photos.sequential_photos.next_photo_to_show_cache import NextPhotoToShowCache

class PhotoToDisplayChooserTests(unittest.TestCase):
    def test_not_being_awake_is_the_primary_decider(self):
        self.awake_decider.are_we_awake.return_value = False
        self.historic_photo_chooser.choose_previous_photo.return_value = 'last'
        self.sequential_photo_chooser.choose_next_photo.return_value = 'next'

        result = self.out.choose_photo()

        self.assertIsNone(result)

    def test_when_awake_the_historic_photo_decides(self):
        self.awake_decider.are_we_awake.return_value = True
        self.historic_photo_chooser.choose_previous_photo.return_value = 'last'
        self.sequential_photo_chooser.choose_next_photo.return_value = 'next'

        result = self.out.choose_photo()

        self.assertEqual(result, 'last')

    def test_when_awake_and_not_looking_back_the_next_photo_is_returned(self):
        self.awake_decider.are_we_awake.return_value = True
        self.historic_photo_chooser.choose_previous_photo.return_value = None
        self.sequential_photo_chooser.choose_next_photo.return_value = 'next'

        result = self.out.choose_photo()

        self.assertEqual(result, 'next')

    def test_when_nothing_is_to_show_show_nothing(self):
        self.awake_decider.are_we_awake.return_value = True
        self.historic_photo_chooser.choose_previous_photo.return_value = None
        self.sequential_photo_chooser.choose_next_photo.return_value = None

        result = self.out.choose_photo()

        self.assertIsNone(result)

    def setUp(self):
        self.awake_decider = Mock(spec=AwakeDecider)
        self.historic_photo_chooser = Mock(spec=HistoricPhotoChooser)
        self.sequential_photo_chooser = Mock(spec=NextPhotoToShowCache)
        self.out = PhotoToDisplayChooser(
            self.awake_decider,
            self.historic_photo_chooser,
            self.sequential_photo_chooser
            )