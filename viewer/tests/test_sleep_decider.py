import unittest
from unittest.mock import Mock

from viewer.src.sleep_decider import SleepDecider


class SleepDeciderTests(unittest.TestCase):
    def test_we_are_awake_until_we_are_not(self):
        self.assertEqual(self.out.are_we_awake(), True)

        self.out.go_to_sleep()
        
        self.assertEqual(self.out.are_we_awake(), False)

    def setUp(self):
        self.out = SleepDecider()
