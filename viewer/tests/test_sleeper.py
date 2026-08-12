import unittest
from unittest.mock import Mock, call

from viewer.src.sleeper import Sleeper


class SleeperTests(unittest.TestCase):
    def test_sleep_until_the_sleep_time_has_elapsed(self):
        self.out.sleep()

        self.assertEqual(
            self.system_operations.get_time_seconds.call_count,
            5)
        self.system_operations.sleep.assert_has_calls(
            [call(0.1),call(0.1),call(0.1)]
        )

    def test_while_sleeping_the_event_handlers_are_called(self):
        self.display.get_events.side_effect = [
            'one', 'two', 'three']

        self.out.sleep()
        
        self.event_handler.handle_events.assert_has_calls(
            [call('one'),call('two'),call('three')]
        )

    @classmethod
    def setUp(self):
        self.system_operations = Mock()
        self.system_operations.get_time_seconds.side_effect = [
            100, 101, 110, 125, 142]
        self.display = Mock()
        self.event_handler = Mock()
        self.out = Sleeper(
            self.system_operations,
            self.display,
            self.event_handler,
            42)
