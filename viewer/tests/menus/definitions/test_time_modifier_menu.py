from datetime import time
import unittest

from viewer.src.menus.definitions.time_modifier_menu import TimeModifierMenu

class TimeModifierMenuTests(unittest.TestCase):
    @unittest.skip("reason for skipping")
    def test_display_time_can_be_increased(self):
        self.out.press('hour up')
        self.out.press('minute up')

        self.assertEqual(self.out.display_time, '11:21')

    @unittest.skip("reason for skipping")
    def test_display_time_can_be_decreased(self):
        self.out.press('hour down')
        self.out.press('minute down')

        self.assertEqual(self.out.display_time, ' 9:19')

    @unittest.skip("reason for skipping")
    def test_changing_display_time_does_no_affect_set_time(self):
        self.out.press('hour up')
        self.out.press('minute up')
        self.assertEqual(self.time,
                         time.fromisoformat('10:20'))
        
        self.out.press('hour down')
        self.out.press('minute down')
        self.assertEqual(self.time,
                         time.fromisoformat('10:20'))

    @unittest.skip("reason for skipping")
    def test_time_is_updated_when_ok_is_pressed(self):
        self.out.press('hour up')
        self.out.press('minute up')
        self.out.press('ok')

        self.assertEqual(self.time, time.fromisoformat('11:21'))

    @unittest.skip("reason for skipping")
    def test_if_get_and_set_not_set_nothing_occurs(self):
        self.out = TimeModifierMenu()
        self.out.press('hour up')
        self.out.press('minute up')
        self.out.press('ok')

        self.assertEqual(self.out.display_time, '--.--')
        self.assertEqual(self.time,
                         time.fromisoformat('10:20'))

    def setUp(self):
        self.out = TimeModifierMenu()
        self.time = time.fromisoformat('10:20')
        self.out.setup(self.get_time, self.set_time)

    def get_time(self):
        return self.time

    def set_time(self, new_time):
        self.time = new_time