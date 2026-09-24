class AwakeSchedule:
    def __init__(self,
                 wake_time,
                 sleep_time,
                 database):
        self._database = database
        self.wake_time = wake_time
        self.sleep_time = sleep_time

    def defuncts(self):
        if self.always_awake:
            return True
        current_time = self._system_operations.get_current_time()
        if current_time >= self.wake_time and current_time < self.sleep_time:
            return True
        return False
    