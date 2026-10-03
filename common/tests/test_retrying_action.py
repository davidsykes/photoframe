import unittest
from unittest.mock import Mock

from common.src.config_file import ConfigFile
from common.src.retrying_action import RetryingAction
from common.src.system_operations import SystemOperations

class RetryingActionTests(unittest.TestCase):
    def test_if_the_action_succeeds_true_is_returned(self):
        self.system_operations.time_monotonic.return_value = 0
        self.action.return_value = True
        #self.system_operations.time_monotonic.side_effect = [0, 1, 2, 3, 4, 5]

        result = self.out.execute(1,2,3)

        self.assertTrue(result)
        self.action.assert_called_once_with(1,2,3)

    def test_if_the_action_fails_once_it_is_retried(self):
        self.system_operations.time_monotonic.side_effect = [0, 1]
        self.action.side_effect = [False, True]

        result = self.out.execute(1,2,3)

        self.assertTrue(result)
        self.action.assert_called_with(1,2,3)
        self.assertEqual(self.action.call_count, 2)
        self.system_operations.sleep.assert_called_with(5)
        self.assertEqual(self.system_operations.sleep.call_count, 1)

    def test_if_the_action_fails_twice_is_is_retried(self):
        self.system_operations.time_monotonic.side_effect = [0, 1, 2]
        self.action.side_effect = [False, False, True]

        result = self.out.execute(1,2,3)

        self.assertTrue(result)
        self.action.assert_called_with(1,2,3)
        self.assertEqual(self.action.call_count, 3)
        self.system_operations.sleep.assert_called_with(5)
        self.assertEqual(self.system_operations.sleep.call_count, 2)

    def test_if_the_action_fails_until_timeout_false_is_returned(self):
        self.system_operations.time_monotonic.side_effect = [0, 10, 32]
        self.action.return_value = False

        result = self.out.execute(1,2,3)

        self.assertFalse(result)
        self.action.assert_called_with(1,2,3)
        self.assertEqual(self.action.call_count, 2)
        self.system_operations.sleep.assert_called_with(5)
        self.assertEqual(self.system_operations.sleep.call_count, 1)

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.action = Mock()
        self.out = RetryingAction(self.action,
                                  self.system_operations,
                                  "action description",
                                  30,
                                  5)