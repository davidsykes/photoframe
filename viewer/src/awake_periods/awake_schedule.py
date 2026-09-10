class AwakeSchedule:
    def __init__(self,
                 system_operations,
                 wake_time,
                 sleep_time,
                 always_awake):
        self._system_operations = system_operations
        self.wake_time = wake_time
        self.sleep_time = sleep_time
        self.always_awake = always_awake

    def are_we_awake(self):
        if self.always_awake:
            return True
        current_time = self._system_operations.get_current_time()
        if current_time >= self.wake_time and current_time < self.sleep_time:
            return True
        return False
    