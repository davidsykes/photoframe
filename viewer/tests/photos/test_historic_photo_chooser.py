import unittest

from viewer.src.photos.historic_photo_chooser import HistoricPhotoChooser
from viewer.src.photos.photo_history import PhotoHistory

class HistoricPhotoChooserTests(unittest.TestCase):
    def test_initially_no_photos_are_returned(self):
        photo = self.out.choose_previous_photo()

        self.assertIsNone(photo)

    def test_when_started_the_last_photo_is_returned(self):
        self.out.enable()

        photo = self.out.choose_previous_photo()

        self.assertEqual('Photo 3', photo)

    def test_photos_can_be_traversed(self):
        self.out.enable()
        self.assertEqual('Photo 3', self.out.choose_previous_photo())

        self.out.back()
        self.assertEqual('Photo 2', self.out.choose_previous_photo())
        self.out.back()
        self.assertEqual('Photo 1', self.out.choose_previous_photo())
        self.out.forward()
        self.assertEqual('Photo 2', self.out.choose_previous_photo())
        self.out.forward()
        self.assertEqual('Photo 3', self.out.choose_previous_photo())

    def test_traversal_stops_at_the_end_and_beginning(self):
        self.out.enable()
        self.assertEqual('Photo 3', self.out.choose_previous_photo())

        self.out.back()
        self.assertEqual('Photo 2', self.out.choose_previous_photo())
        self.out.back()
        self.assertEqual('Photo 1', self.out.choose_previous_photo())
        self.out.back()
        self.assertEqual('Photo 1', self.out.choose_previous_photo())
        self.out.back()
        self.assertEqual('Photo 1', self.out.choose_previous_photo())
        self.out.forward()
        self.assertEqual('Photo 2', self.out.choose_previous_photo())
        self.out.forward()
        self.assertEqual('Photo 3', self.out.choose_previous_photo())
        self.out.forward()
        self.assertEqual('Photo 3', self.out.choose_previous_photo())
        self.out.forward()
        self.assertEqual('Photo 3', self.out.choose_previous_photo())

    def test_disabling_returns_returns_to_none(self):
        self.out.enable()
        self.out.disable()
        self.assertEqual(None, self.out.choose_previous_photo())

    def setUp(self):
        self.photo_history = PhotoHistory(3)
        self.photo_history.new_photo('Photo 1')
        self.photo_history.new_photo('Photo 2')
        self.photo_history.new_photo('Photo 3')
        self.out = HistoricPhotoChooser(self.photo_history)