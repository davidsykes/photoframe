import unittest
from unittest.mock import Mock

from viewer.src.menus.framework.menu_items.menu_touch_area import MenuTouchArea

class MenuTouchAreaTests(unittest.TestCase):
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

    def test_mouse_hits_return_action_value(self):
        self.assertIsNone(self.out.mouse_down(self.x-1, self.y))
        self.assertEqual('value', self.out.mouse_down(self.x, self.y))

    def setUp(self):
        self.x = 123
        self.y = 456
        width = 100
        height = 150
        self.x2 = self.x + width - 1
        self.y2 = self.y + height - 1
        self.out = MenuTouchArea('name',
                                 action=self.action,
                                 rect_xywh=(self.x, self.y, width, height))
        self.action_count = 0

    def action(self):
        self.action_count += 1
        return 'value'

    def mouse_miss(self, x, y):
        expected = self.action_count
        self.out.mouse_down(x, y)
        self.assertEqual(expected, self.action_count)

    def mouse_hit(self, x, y):
        expected = self.action_count + 1
        self.out.mouse_down(x, y)
        self.assertEqual(expected, self.action_count)
