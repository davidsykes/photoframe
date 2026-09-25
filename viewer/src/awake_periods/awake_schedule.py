class AwakeSchedule:
    def __init__(self, database):
        self._database = database
        DEFAULT_WAKE_TIME = '08:30'
        DEFAULT_SLEEP_TIME = '19:45'
        self._initialise_schedule_times(DEFAULT_WAKE_TIME, DEFAULT_SLEEP_TIME)

    def _initialise_schedule_times(self, wake_time, sleep_time):
        self.wake_time = (
            self._database.get_setting('wake_time')
            or wake_time)
        self.sleep_time = (
            self._database.get_setting('sleep_time')
            or sleep_time)

    def defuncts(self):
        if self.always_awake:
            return True
        current_time = self._system_operations.get_current_time()
        if current_time >= self.wake_time and current_time < self.sleep_time:
            return True
        return False
    