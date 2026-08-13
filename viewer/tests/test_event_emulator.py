import unittest
from unittest.mock import Mock, call

from viewer.src.action_timer import ActionTimer
from viewer.src.menus.event_emulator import EventEmulator


class EventEmulatorTests(unittest.TestCase):
    def test_events_appear_when_they_are_ready(self):
        self.out.set_events([
            (10,'Set 1'),
            (20,'Set 2'),
        ])

        self.assertEqual(self.out.get_events(), [])
        self.set_time(9)
        self.assertEqual(self.out.get_events(), [])
        self.set_time(10)
        self.assertEqual(self.out.get_events(), 'Set 1')
        self.assertEqual(self.out.get_events(), [])
        self.set_time(19)
        self.assertEqual(self.out.get_events(), [])
        self.set_time(20)
        self.assertEqual(self.out.get_events(), 'Set 2')
        self.assertEqual(self.out.get_events(), [])

    @classmethod
    def setUp(self):
        self.system_operations = Mock()
        self.system_operations.get_time_seconds = Mock()
        self.base_time = 345
        self.set_time(self, 0)
        self.out = EventEmulator(
            self.system_operations)

    def set_time(self, time):
        current_time = self.base_time + time
        self.system_operations.get_time_seconds.return_value = current_time
