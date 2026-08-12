import unittest
from unittest.mock import Mock, call

from viewer.src.sleeper import Sleeper


class SleeperTests(unittest.TestCase):
    def test_sleep_until_the_sleep_time_has_elapsed(self):
        self.system_operations.time.side_effect = [
            100, 101, 110, 125, 142]

        self.out.sleep()

        self.assertEqual(
            self.system_operations.time.call_count,
            5)
        self.system_operations.sleep.assert_has_calls(
            [call(0.1),call(0.1),call(0.1)]
        )


    @classmethod
    def setUp(self):
        self.system_operations = Mock()
        self.out = Sleeper(
            self.system_operations,
            42)

    def side_effect(path):
        return 'image ' + path
