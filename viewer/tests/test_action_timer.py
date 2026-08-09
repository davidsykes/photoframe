import unittest
from unittest.mock import Mock, call

from viewer.src.action_timer import ActionTimer


class ActionTimerTests(unittest.TestCase):
    def test_actions_are_not_triggered_before_it_is_time(self):
        self.wait_time(9)

        self.out.poll()

        self.action.assert_not_called()
        
    def test_actions_are_triggered_when_it_is_time(self):
        self.wait_time(10)

        self.out.poll()

        self.action.assert_called_once()
        
    def test_actions_are_not_repeated_until_it_is_time(self):
        self.wait_time(10)
        self.out.poll()
        self.wait_time(9)
        self.out.poll()

        self.assertEqual(self.action.call_count, 1)
        
    def test_actions_are_repeated_every_time(self):
        self.wait_time(10)
        self.out.poll()
        self.wait_time(10)
        self.out.poll()

        self.assertEqual(self.action.call_count, 2)
        
    def test_subsequent_actions_are_timed_from_their_previous_execution(self):
        self.wait_time(12)
        self.out.poll()
        self.assertEqual(self.action.call_count, 1)

        self.wait_time(9)
        self.out.poll()
        self.assertEqual(self.action.call_count, 1)

        self.wait_time(1)
        self.out.poll()
        self.assertEqual(self.action.call_count, 2)

    @classmethod
    def setUp(self):
        self.system_operations = Mock()
        self.system_operations.get_time = Mock()
        self.current_time = 0
        self.wait_time(self, 123)
        self.action = Mock()
        self.out = ActionTimer(
            self.system_operations,
            self.action,
            10)

    def wait_time(self, time):
        self.current_time += time
        self.system_operations.get_time.return_value = self.current_time
