import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from viewer.src.action_timer import ActionTimer


class ActionTimerTests(unittest.TestCase):
    def test_an_action_is_triggered_on_the_first_call(self):
        self.assert_call_returns(1)

    def test_actions_are_not_triggered_before_it_is_time(self):
        self.out.run_if_due()
        self.wait_time(9)

        self.assert_call_returns(None)

    def test_actions_are_triggered_when_it_is_time(self):
        self.out.run_if_due()
        self.wait_time(10)

        self.assert_call_returns(2)

    def test_actions_are_not_repeated_until_it_is_time(self):
        self.out.run_if_due()
        self.wait_time(10)
        self.out.run_if_due()
        self.wait_time(9)
        
        self.assert_call_returns(None)

    def test_actions_are_repeated_every_time(self):
        self.out.run_if_due()
        self.wait_time(10)
        self.out.run_if_due()
        self.wait_time(10)

        self.assert_call_returns(3)

    def test_subsequent_actions_are_timed_from_their_previous_execution(self):
        self.out.run_if_due()
        self.wait_time(12)
        self.assert_call_returns(2)

        self.wait_time(9)
        self.assert_call_returns(None)

        self.wait_time(1)
        self.assert_call_returns(3)

    @classmethod
    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.system_operations.get_time_seconds = Mock()
        self.current_time = 0
        self.wait_time(self, 123)
        self.action = Mock()
        self.action.side_effect  = [1,2,3]
        self.out = ActionTimer(
            self.system_operations,
            self.action,
            10)

    def wait_time(self, time):
        self.current_time += time
        self.system_operations.get_time_seconds.return_value = self.current_time

    def assert_call_returns(self, value):
        v = self.out.run_if_due()
        self.assertEqual(v, value)
