from datetime import time
import unittest
from unittest.mock import Mock

from viewer.src.sleep.awake_period_generator import AwakePeriodGenerator
from viewer.src.status.application_status import ApplicationStatus

class AwakePeriodGeneratorTests(unittest.TestCase):
    def test_a_simple_time_period_is_generated(self):
        tp = self.out.generate_awake_period("10:00", "20:00")
        self.assertEqual(tp.start_time, time.fromisoformat("10:00"))
        self.assertEqual(tp.end_time, time.fromisoformat("20:00"))

    def setUp(self):
        self.application_status = Mock(spec=ApplicationStatus)
        self.out = AwakePeriodGenerator(self.application_status)
