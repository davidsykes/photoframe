import unittest
from unittest.mock import Mock

from viewer.src.action_timer import ActionTimer
from viewer.src.images.image_loader import ImageLoader
from viewer.src.images.image_provider import ImageProvider


class ImageProviderTests(unittest.TestCase):
    def test_when_a_new_image_is_available_it_is_loaded(self):
        self.next_image_timer.run_if_due.return_value = 'new image'

        image = self.out.provide_image()

        self.assertEqual(image, 'image at new image')

    def test_an_image_is_cached_until_the_next_image(self):
        self.next_image_timer.run_if_due.return_value = 'image'
        self.assertEqual(self.out.provide_image(), 'image at image')

        self.next_image_timer.run_if_due.return_value = None
        self.assertEqual(self.out.provide_image(), 'image at image')
        self.assertEqual(self.out.provide_image(), 'image at image')
        self.assertEqual(self.out.provide_image(), 'image at image')

        self.next_image_timer.run_if_due.return_value = 'new image'
        self.assertEqual(self.out.provide_image(), 'image at new image')

    def test_when_sleep_decider_says_sleep_no_image_is_provided(self):
        self.next_image_timer.run_if_due.return_value = 'image'
        self.sleep_decider.are_we_awake.return_value = False

        self.assertEqual(self.out.provide_image(), None)

    def setUp(self):
        self.next_image_timer = Mock(spec=ActionTimer)
        self.image_loader = Mock(spec=ImageLoader)
        self.image_loader.load_image = self.mock_image_loader_load_image
        self.sleep_decider = Mock()
        self.sleep_decider.are_we_awake.return_value = True
        self.out = ImageProvider(
            self.next_image_timer,
            self.image_loader,
            self.sleep_decider)

    def mock_image_loader_load_image(self, path):
        return 'image at ' + path