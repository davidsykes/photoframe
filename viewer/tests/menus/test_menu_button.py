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

    def test_mouse_down_coordinates(self):
        self.mouse_miss(self.x-1, self.y)
        self.mouse_miss(self.x, self.y-1)
        self.mouse_hit(self.x, self.y)
        
        self.mouse_miss(self.x2+1, self.y)
        self.mouse_miss(self.x2, self.y-1)
        self.mouse_hit(self.x2, self.y)
        
        self.mouse_miss(self.x-1, self.y2)
        self.mouse_miss(self.x, self.y2+1)
        self.mouse_hit(self.x, self.y2)
        
        self.mouse_miss(self.x2+1, self.y2)
        self.mouse_miss(self.x2, self.y2+1)
        self.mouse_hit(self.x2, self.y2)

    def setUp(self):
        self.display = Mock()
        self.display.COLOUR_LIGHT = 'light colour'
        self.display.COLOUR_WHITE = 'white colour'
        self.x = 123
        self.y = 456
        width = 100
        height = 150
        self.x2 = self.x + width - 1
        self.y2 = self.y + height - 1
        self.out = MenuButton(self.x, self.y,
                              width, height,
                              'button text',
                              self.action)
        self.action_count = 0

    def action(self):
        self.action_count += 1

    def mouse_miss(self, x, y):
        expected = self.action_count
        self.out.mouse_down(x, y)
        self.assertEqual(expected, self.action_count)

    def mouse_hit(self, x, y):
        expected = self.action_count + 1
        self.out.mouse_down(x, y)
        self.assertEqual(expected, self.action_count)
