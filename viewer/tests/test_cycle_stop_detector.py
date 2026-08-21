import unittest
from unittest.mock import Mock, call

from viewer.src.cycle_stop_detector import CycleStopDetector


class CycleStopDetectorTests(unittest.TestCase):
    def test_no_stop_if_nothing_wants_to(self):
        stop = self.out.poll()

        self.assertFalse(stop)
        
    def test_stop_if_1_wants_to(self):
        self.reason1.run_if_due.return_value = True

        stop = self.out.poll()

        self.assertTrue(stop)
        
    def test_stop_if_2_wants_to(self):
        self.reason2.run_if_due.return_value = True

        stop = self.out.poll()

        self.assertTrue(stop)
        
    def test_stop_if_3_wants_to(self):
        self.reason3.run_if_due.return_value = True

        stop = self.out.poll()

        self.assertTrue(stop)

    @classmethod
    def setUp(self):
        self.reason1 = Mock()
        self.reason1.run_if_due.return_value = False
        self.reason2 = Mock()
        self.reason2.run_if_due.return_value = False
        self.reason3 = Mock()
        self.reason3.run_if_due.return_value = False
        self.out = CycleStopDetector(
            [self.reason1,
             self.reason2,
             self.reason3])