import unittest
from unittest.mock import Mock

from viewer.src.menus.framework.menu_items.menu_button_text import MenuButtonText

class MenuButtonTextTests(unittest.TestCase):
    def test_menu_buttons_are_rendered(self):
        self.out.render(self.display)

        self.display.draw_rectangle.assert_called_once_with(
            'light colour',
            (123, 456, 100, 150)
        )

        self.display.wrapper.draw_text.assert_called_once_with(
            'button text',
            (124, 457)
        )

    def test_menu_buttons_can_be_activated(self):
        self.out.activate(123, 456)

        self.assertEqual(1, self.action_count)

    def setUp(self):
        self.display = Mock()
        self.display.COLOUR_LIGHT = 'light colour'
        # self.display.COLOUR_WHITE = 'white colour'
        self.x = 123
        self.y = 456
        width = 100
        height = 150
        self.out = MenuButtonText('button text',
                               (self.x, self.y,
                               width, height),
                               self.action,)
        self.action_count = 0

    def action(self):
        self.action_count += 1
        return 'value'
