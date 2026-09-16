import unittest
from unittest.mock import Mock
from viewer.src.action_timer import ActionTimer
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

    def setUp(self):
        self.next_image_timer = Mock(spec=ActionTimer)
        # self.image_loader = Mock(spec=ImageFromFileLoader)
        # self.image_loader.load_image = self.mock_image_loader_load_image
        # self.awake_decider = Mock()
        # self.awake_decider.are_we_awake.return_value = True
        self.out = SequentialPhotoChooser(
            self.next_image_timer)
