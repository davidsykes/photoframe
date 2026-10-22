import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from viewer.src.menus.framework.events_emulator import EventsEmulator
from viewer.src.data.uievent import UIEvent, UIEventType


class EventsEmulatorTests(unittest.TestCase):
    def test_events_appear_when_they_are_ready(self):
        self.out.set_events([
            (10, 1,2),
            (20, 3,4),
        ])

        self.assertEqual(self.out.get_events(), [])
        self.set_time(9)
        self.assertEqual(self.out.get_events(), [])
        self.set_time(10)
        self.assertEqual(self.out.get_events(),
                         [UIEvent(UIEventType.MOUSE_DOWN, 1,2)])
        self.assertEqual(self.out.get_events(), [])
        self.set_time(19)
        self.assertEqual(self.out.get_events(), [])
        self.set_time(20)
        self.assertEqual(self.out.get_events(),
                         [UIEvent(UIEventType.MOUSE_DOWN, 3,4)])
        self.assertEqual(self.out.get_events(), [])

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.system_operations.get_time_seconds = Mock()
        self.base_time = 345
        self.set_time(0)
        self.out = EventsEmulator(
            self.system_operations)

    def set_time(self, time):
        current_time = self.base_time + time
        self.system_operations.get_time_seconds.return_value = current_time
