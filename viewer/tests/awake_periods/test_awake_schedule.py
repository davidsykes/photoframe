from datetime import time
import datetime
import unittest

from viewer.src.awake_periods.awake_schedule import AwakeSchedule


class AwakeScheduleTests(unittest.TestCase):
    def test_we_are_awake_when_it_is_time(self):
        self.assertFalse(self.out.are_we_awake(datetime.time(0, 00)))
        self.assertFalse(self.out.are_we_awake(datetime.time(7, 30)))
        self.assertFalse(self.out.are_we_awake(datetime.time(9, 59)))
        self.assertTrue(self.out.are_we_awake(datetime.time(10, 00)))
        self.assertTrue(self.out.are_we_awake(datetime.time(10, 1)))
        self.assertTrue(self.out.are_we_awake(datetime.time(15, 00)))
        self.assertTrue(self.out.are_we_awake(datetime.time(19, 59)))
        self.assertFalse(self.out.are_we_awake(datetime.time(20, 00)))
        self.assertFalse(self.out.are_we_awake(datetime.time(23, 59)))

    def setUp(self):
        wake_time = time.fromisoformat("10:00")
        sleep_time = time.fromisoformat("20:00")
        self.out = AwakeSchedule(wake_time, sleep_time)
