import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from viewer.src.action_timer import ActionTimer


class ActionTimerTests(unittest.TestCase):
    def test_an_action_is_triggered_on_the_first_call_and_then_repeated(self):
        self.assert_call_at_time_returns(0, 1)
        self.assert_call_at_time_returns(9, None)
        self.assert_call_at_time_returns(10, 2)
        self.assert_call_at_time_returns(19, None)
        self.assert_call_at_time_returns(20, 3)
        self.assert_call_at_time_returns(29, None)

    def test_actions_are_timed_from_the_previous_change(self):
        self.assert_call_at_time_returns(0, 1)
        self.assert_call_at_time_returns(9, None)
        self.assert_call_at_time_returns(110, 2)
        self.assert_call_at_time_returns(119, None)
        self.assert_call_at_time_returns(120, 3)
        self.assert_call_at_time_returns(129, None)

    def test_action_time_can_be_paused(self):
        self.assert_call_at_time_returns(0, 1)
        self.assert_call_at_time_returns(10, 2)

        self.out.pause()

        self.assert_call_at_time_returns(100, None)

        self.out.resume()

        self.assert_call_at_time_returns(100, 3)
        self.assert_call_at_time_returns(109, None)
        self.assert_call_at_time_returns(110, 4)

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.start_of_time = 123
        self.action = Mock()
        self.action.side_effect  = [1,2,3,4]
        self.out = ActionTimer(
            'name',
            self.system_operations,
            self.action,
            10)

    def assert_call_at_time_returns(self, current_time, return_value):
        self.current_time = self.start_of_time + current_time
        self.system_operations.get_time_seconds.return_value = self.current_time
        v = self.out.run_if_due()
        self.assertEqual(v, return_value)
