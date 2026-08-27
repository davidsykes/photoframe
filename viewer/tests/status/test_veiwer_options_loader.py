import unittest
from unittest.mock import Mock, call

from viewer.src.status.viewer_options_loader import ViewerOptionsLoader


class ViewerOpionsLoaderTests(unittest.TestCase):
    def test_default_values_are_set(self):
        opts = self.out.load_viewer_options([])

        self.assertFalse(opts.show_image_names)

    def test_show_images_can_be_set(self):
        opts = self.out.load_viewer_options(['si'])

        self.assertTrue(opts.show_image_names)

    @classmethod
    def setUp(self):
        self.out = ViewerOptionsLoader()
