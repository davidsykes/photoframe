from datetime import time
import datetime
import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from viewer.src.awake_periods.awake_schedule import AwakeSchedule


class AwakeScheduleTests(unittest.TestCase):
    def test_we_are_awake_when_it_is_time(self):
        self.system_operations.get_current_time.return_value = datetime.time(0, 0)
        self.assertFalse(self.out.are_we_awake())
        self.system_operations.get_current_time.return_value = datetime.time(7, 30)
        self.assertFalse(self.out.are_we_awake())
        self.system_operations.get_current_time.return_value = datetime.time(9, 59)
        self.assertFalse(self.out.are_we_awake())
        self.system_operations.get_current_time.return_value = datetime.time(10, 00)
        self.assertTrue(self.out.are_we_awake())
        self.system_operations.get_current_time.return_value = datetime.time(10, 1)
        self.assertTrue(self.out.are_we_awake())
        self.system_operations.get_current_time.return_value = datetime.time(15, 00)
        self.assertTrue(self.out.are_we_awake())
        self.system_operations.get_current_time.return_value = datetime.time(19, 59)
        self.assertTrue(self.out.are_we_awake())
        self.system_operations.get_current_time.return_value = datetime.time(20, 00)
        self.assertFalse(self.out.are_we_awake())
        self.system_operations.get_current_time.return_value = datetime.time(23, 59)
        self.assertFalse(self.out.are_we_awake())

    def setUp(self):
        self.system_operations = Mock(spec = SystemOperations)
        wake_time = time.fromisoformat("10:00")
        sleep_time = time.fromisoformat("20:00")
        self.out = AwakeSchedule(self.system_operations, wake_time, sleep_time)
