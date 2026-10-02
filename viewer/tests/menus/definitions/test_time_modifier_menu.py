from datetime import time
import unittest
from unittest.mock import Mock

from viewer.src.menus.definitions.time_modifier_menu import TimeModifierMenu

class TimeModifierMenuTests(unittest.TestCase):
    def test_menu_items_are_created(self):
        self.assertEqual(len(self.out._buttons), 10)
        self.assertEqual(self.out._buttons[0].name, 'title_text')
        self.assertEqual(self.out._buttons[1].name, 'time_display_text')
        self.assertEqual(self.out._buttons[2].name, 'hour up')
        self.assertEqual(self.out._buttons[3].name, 'minute up')
        self.assertEqual(self.out._buttons[4].name, 'hour_text')
        self.assertEqual(self.out._buttons[5].name, 'minute_text')
        self.assertEqual(self.out._buttons[6].name, 'hour down')
        self.assertEqual(self.out._buttons[7].name, 'minute down')
        self.assertEqual(self.out._buttons[8].name, 'Ok')

    def test_menu_items_are_displayed(self):
        self.out.render(self.display)
        self.assertTrue('Time to modify' in self.display.rendered_text)
        self.assertTrue('10:20' in self.display.rendered_text)
        self.assertTrue('Hour' in self.display.rendered_text)
        self.assertTrue('Minute' in self.display.rendered_text)
        self.assertTrue('+' in self.display.rendered_text)
        self.assertTrue('-' in self.display.rendered_text)

    def test_display_time_can_be_increased(self):
        self.out.press('hour up')
        self.out.press('minute up')

        self.assertEqual(self.out.display_time,
                         time.fromisoformat('11:21'))
        self.assertEqual(self.get_display_time(),
                         '11:21')

    def test_display_time_can_be_decreased(self):
        self.out.press('hour down')
        self.out.press('minute down')

        self.assertEqual(self.out.display_time,
                         time.fromisoformat('09:19'))
        self.assertEqual(self.get_display_time(),
                         '09:19')

    def test_changing_display_time_does_no_affect_set_time(self):
        self.out.press('hour up')
        self.out.press('minute up')
        self.assertEqual(self.time,
                         time.fromisoformat('10:20'))
        
        self.out.press('hour down')
        self.out.press('minute down')
        self.assertEqual(self.time,
                         time.fromisoformat('10:20'))

    def test_time_is_updated_when_ok_is_pressed(self):
        self.out.press('hour up')
        self.out.press('minute up')
        self.out.press('Ok')

        self.assertEqual(self.time, time.fromisoformat('11:21'))

    def test_if_get_and_set_not_set_time_display_defaults_to_undefined(self):
        self.out = TimeModifierMenu()

        self.assertEqual(self.get_display_time(), '--:--')

    def test_if_get_and_set_not_set_time_defaults_internally_to_mid_day(self):
        self.out = TimeModifierMenu()
        self.out.press('hour up')
        self.out.press('minute up')

        self.assertEqual(self.out.display_time,
                         time.fromisoformat('13:01'))

    def setUp(self):
        self.display = Mock()
        self.display.rendered_text = {}
        self.display.draw_text = self.draw_text
        self.out = TimeModifierMenu()
        self.time = time.fromisoformat('10:20')
        self.out.setup('Time to modify', self.get_time, self.set_time)

    def get_time(self):
        return self.time

    def set_time(self, new_time):
        self.time = new_time

    def get_display_time(self):
        return self.out._time_display._display_text

    def draw_text(self, text, colour, coordinates):
        self.display.rendered_text[text] = (colour, coordinates)