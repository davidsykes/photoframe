import unittest
from unittest.mock import Mock
from datetime import time

from viewer.src.awake_periods.awake_schedule import AwakeSchedule

class AwakeScheduleTests(unittest.TestCase):
    def test_if_database_settings_are_missing_the_defaults_are_used(self):
        self.create_test_object()
        
        self.assertEqual(time.fromisoformat('08:30'), self.out.get_wake_time())
        self.assertEqual(time.fromisoformat('19:45'), self.out.get_sleep_time())

    def test_database_wake_settings_are_taken_if_they_exist(self):
        self.database_data = {'wake_time': '11:11'}

        self.create_test_object()
        
        self.assertEqual(time.fromisoformat('11:11'), self.out.get_wake_time())
        self.assertEqual(time.fromisoformat('19:45'), self.out.get_sleep_time())

    def test_database_sleep_settings_are_taken_if_they_exist(self):
        self.database_data = {'sleep_time': '22:22'}

        self.create_test_object()
        
        self.assertEqual(time.fromisoformat('08:30'), self.out.get_wake_time())
        self.assertEqual(time.fromisoformat('22:22'), self.out.get_sleep_time())

    def test_both_database_settings_are_taken_if_they_exist(self):
        self.database_data = {'wake_time': '11:11', 'sleep_time': '22:22'}

        self.create_test_object()
        
        self.assertEqual(time.fromisoformat('11:11'), self.out.get_wake_time())
        self.assertEqual(time.fromisoformat('22:22'), self.out.get_sleep_time())

    def test_set_wake_time_updates_local_value(self):
        self.create_test_object()

        self.out.set_wake_time(time.fromisoformat('12:34'))
        
        self.assertEqual(time.fromisoformat('12:34'), self.out.get_wake_time())

    def test_set_wake_time_updates_database_value(self):
        self.create_test_object()

        self.out.set_wake_time(time.fromisoformat('12:34'))

        self.database.set_setting.assert_called_once_with(
            'wake_time', '12:34')

    def test_set_sleep_time_updates_local_value(self):
        self.create_test_object()

        self.out.set_sleep_time(time.fromisoformat('12:34'))
        
        self.assertEqual(time.fromisoformat('12:34'), self.out.get_sleep_time())

    def test_set_sleep_time_updates_database_value(self):
        self.create_test_object()

        self.out.set_sleep_time(time.fromisoformat('12:34'))

        self.database.set_setting.assert_called_once_with(
            'sleep_time', '12:34')

    def setUp(self):
        self.database = Mock()
        self.database.get_setting = self.get_setting
        self.database_data = {}

    def create_test_object(self):
        self.out = AwakeSchedule(self.database)

    def get_setting(self, name):
        if name in self.database_data:
            return self.database_data[name]
        return None