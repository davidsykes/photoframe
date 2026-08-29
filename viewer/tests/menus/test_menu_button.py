import unittest
from unittest.mock import Mock, call

from viewer.src.menus.menu_button import MenuButton


class MenuButtonTests(unittest.TestCase):
    def test_menu_buttons_are_rendered(self):
        self.out.render(self.display)

        self.display.draw_rectangle.assert_called_once_with(
            'colour',
            (123, 456, 100, 150)
        )

    def setUp(self):
        self.display = Mock()
        self.display.COLOUR_LIGHT = 'colour'
        self.out = MenuButton(123, 456, 100, 150, 'button text')
