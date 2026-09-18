import unittest
from unittest.mock import Mock, call
from viewer.src.action_timer import ActionTimer
from viewer.src.photos.photo_history import PhotoHistory
from viewer.src.photos.sequential_photos.sequential_photo_chooser import SequentialPhotoChooser


class SequentialPhotoChooserTests(unittest.TestCase):
    def test_choose_next_photo_is_a_wrapper_for_action_timer(self):
        self.next_image_timer.run_if_due.return_value = 'next photo'

        photo = self.out.choose_next_photo()

        self.assertEqual(photo, 'next photo')

    def test_choose_next_photo_caches_the_last_timer_result(self):
        self.next_image_timer.run_if_due.side_effect = [
            'photo 1', None, None, 'photo 2', None]

        self.assertEqual(self.out.choose_next_photo(), 'photo 1')
        self.assertEqual(self.out.choose_next_photo(), 'photo 1')
        self.assertEqual(self.out.choose_next_photo(), 'photo 1')
        self.assertEqual(self.out.choose_next_photo(), 'photo 2')
        self.assertEqual(self.out.choose_next_photo(), 'photo 2')

    def test_photo_history_is_updated_when_photos_change(self):
        self.next_image_timer.run_if_due.side_effect = [
            'photo 1', None, 'photo 2', None, 'photo 3']

        self.out.choose_next_photo()
        self.out.choose_next_photo()
        self.out.choose_next_photo()
        self.out.choose_next_photo()
        self.out.choose_next_photo()

        self.photo_history.new_photo.assert_has_calls(
            [call('photo 1'),call('photo 2'),call('photo 3')]
        )

    def setUp(self):
        self.next_image_timer = Mock(spec=ActionTimer)
        self.photo_history = Mock(spec=PhotoHistory)
        self.out = SequentialPhotoChooser(
            self.next_image_timer,
            self.photo_history)
