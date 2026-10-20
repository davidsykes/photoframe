import unittest
from unittest.mock import Mock

from viewer.src.display.display_wrapper import DisplayWrapper


class DisplayWrapperTests(unittest.TestCase):
    def test_simple_text_is_displayed(self):
        command = self.out.draw_text(
            'text',
            (12,34)
        )

        self.display.draw_rectangle.assert_not_called()
        self.display.draw_rendered_text.assert_called_once_with(
            self.rendered_text,
            (12,34)
        )


    def setUp(self):
        self.rendered_text = Mock()
        self.display = Mock()
        self.display.render_text = self.render_text
        self.out = DisplayWrapper(self.display)

    def render_text(self, text):
        if text == 'text':
            return self.rendered_text