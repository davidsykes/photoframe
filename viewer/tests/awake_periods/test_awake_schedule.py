import unittest
from unittest.mock import Mock

from viewer.src.awake_periods.awake_schedule import AwakeSchedule

class AwakeScheduleTests(unittest.TestCase):
    def test_if_database_settings_are_missing_the_defaults_are_used(self):
        self.database_data = {}

        self.create_test_object()
        
        self.assertEqual('08:30', self.out.wake_time)
        self.assertEqual('19:45', self.out.sleep_time)

    def test_database_wake_settings_are_taken_if_they_exist(self):
        self.database_data = {'wake_time': '11:11'}

        self.create_test_object()
        
        self.assertEqual('11:11', self.out.wake_time)
        self.assertEqual('19:45', self.out.sleep_time)

    def test_database_sleep_settings_are_taken_if_they_exist(self):
        self.database_data = {'sleep_time': '22:22'}

        self.create_test_object()
        
        self.assertEqual('08:30', self.out.wake_time)
        self.assertEqual('22:22', self.out.sleep_time)

    def test_both_database_settings_are_taken_if_they_exist(self):
        self.database_data = {'wake_time': '11:11', 'sleep_time': '22:22'}

        self.create_test_object()
        
        self.assertEqual('11:11', self.out.wake_time)
        self.assertEqual('22:22', self.out.sleep_time)

    def setUp(self):
        self.database = Mock()
        self.database.get_setting = self.get_setting

    def create_test_object(self):
        self.out = AwakeSchedule(self.database)

    def get_setting(self, name):
        if name in self.database_data:
            return self.database_data[name]
        return None