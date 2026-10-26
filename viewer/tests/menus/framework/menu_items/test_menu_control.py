import unittest
from unittest.mock import Mock

from viewer.src.menus.framework.menu_items.menu_control import MenuControl


class MenuControlTests(unittest.TestCase):
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

    def test_area_can_come_from_a_rect(self):
        control = MenuControl('control',
                              self.action,
                              rect_xywh=(1,2,3,4))

        self.assertEqual(control._rect_xywh, (1,2,3,4))

    def test_area_can_come_from_position_and_size(self):
        control = MenuControl('control',
                              self.action,
                              position=(1,2),
                              size=(3,4))

        self.assertEqual(control._rect_xywh, (1,2,3,4))

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
        self.out = MenuControl('control',
                               self.action,
                               rect_xywh=(self.x, self.y,
                                          width, height),
                              )
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
