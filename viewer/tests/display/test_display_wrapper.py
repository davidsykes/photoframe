import unittest
from unittest.mock import Mock

from viewer.src.display.display_wrapper import DisplayWrapper


class DisplayWrapperTests(unittest.TestCase):
    def test_simple_text_is_displayed(self):
        self.out.draw_text(
            'text',
            (12,34)
        )

        self.display.draw_rectangle.assert_not_called()
        self.display.draw_rendered_text.assert_called_once_with(
            self.rendered_text,
            (12,34)
        )

    def test_load_image_from_file_and_scale_loads_and_scales(self):
        self.display.load_image.return_value = 'image'
        self.display.scale_image.return_value = 'scaled image'

        image = self.out.load_image_from_file_and_scale(
            'image path',
            (12,34)
        )

        self.display.load_image.assert_called_once_with(
            'image path'
        )

        self.display.scale_image.assert_called_once_with(
            'image', (12,34))

        self.assertEqual('scaled image', image)

    def test_show_image_shows_the_image(self):
        self.out.show_image('image', (12,34))

        self.display.show_image.assert_called_once_with(
            'image', (12,34)
        )

    def setUp(self):
        self.rendered_text = Mock()
        self.display = Mock()
        self.display.render_text = self.render_text
        self.out = DisplayWrapper(self.display)

    def render_text(self, text):
        if text == 'text':
            return self.rendered_text