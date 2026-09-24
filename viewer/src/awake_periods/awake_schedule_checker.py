class AwakeScheduleChecker:
    def __init__(self,
                 system_operations,
                 awake_schedule,
                 always_awake):
        self._system_operations = system_operations
        self._awake_schedule = awake_schedule
        self.always_awake = always_awake

    def are_we_awake(self):
        if self.always_awake:
            return True
        current_time = self._system_operations.get_current_time()
        if current_time >= self._awake_schedule.wake_time and current_time < self._awake_schedule.sleep_time:
            return True
        return False
    