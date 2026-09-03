class AwakeSchedule:
    def __init__(self,
                 system_operations,
                 wake_time,
                 sleep_time):
        self._system_operations = system_operations
        self.wake_time = wake_time
        self.sleep_time = sleep_time

    def are_we_awake(self):
        current_time = self._system_operations.get_current_time()
        print(f'Current time: {current_time}, wake time: {self.wake_time}, sleep time: {self.sleep_time}')
        if current_time >= self.wake_time and current_time < self.sleep_time:
            return True
        return False
    