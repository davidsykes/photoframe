import unittest
from unittest.mock import Mock
from viewer.src.action_timer import ActionTimer
from viewer.src.photos.sequential_photos.sequential_photo_chooser import SequentialPhotoChooser


class SequentialPhotoChooserTests(unittest.TestCase):
    def test_choose_next_photo_is_a_wrapper_for_action_timer(self):
        self.next_image_timer.run_if_due.return_value = 'next photo'

        photo = self.out.choose_next_photo()

        self.assertEqual(photo, 'next photo')

    def setUp(self):
        self.next_image_timer = Mock(spec=ActionTimer)
        # self.image_loader = Mock(spec=ImageFromFileLoader)
        # self.image_loader.load_image = self.mock_image_loader_load_image
        # self.awake_decider = Mock()
        # self.awake_decider.are_we_awake.return_value = True
        self.out = SequentialPhotoChooser(
            self.next_image_timer)
