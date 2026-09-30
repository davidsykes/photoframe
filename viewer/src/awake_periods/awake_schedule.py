from datetime import time


class AwakeSchedule:
    def __init__(self, database):
        self._database = database
        DEFAULT_WAKE_TIME = '08:30'
        DEFAULT_SLEEP_TIME = '19:45'
        self._initialise_schedule_times(DEFAULT_WAKE_TIME, DEFAULT_SLEEP_TIME)

    def _initialise_schedule_times(self, wake_time, sleep_time):
        self._wake_time = time.fromisoformat(
            self._database.get_setting('wake_time')
            or wake_time)
        self._sleep_time = time.fromisoformat(
            self._database.get_setting('sleep_time')
            or sleep_time)

    def get_wake_time(self):
        return self._wake_time

    def set_wake_time(self, wake_time):
        raise 'ssdfafdsf'

    def get_sleep_time(self):
        return self._sleep_time

    def set_sleep_time(self, wake_time):
        raise 'ssdfafdsf'