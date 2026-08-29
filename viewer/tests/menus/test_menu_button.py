import unittest
from unittest.mock import Mock, call

from viewer.src.menus.menu_button import MenuButton


class MenuButtonTests(unittest.TestCase):
    def test_menu_buttons_are_rendered(self):
        self.out.render(self.display)

        self.display.draw_rectangle.assert_called_once_with(
            'light colour',
            (123, 456, 100, 150)
        )

        self.display.draw_text.assert_called_once_with(
            'button text',
            'white colour',
            (123, 456)
        )

    def setUp(self):
        self.display = Mock()
        self.display.COLOUR_LIGHT = 'light colour'
        self.display.COLOUR_WHITE = 'white colour'
        self.out = MenuButton(123, 456, 100, 150, 'button text')
