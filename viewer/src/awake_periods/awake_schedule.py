class AwakeSchedule:
    def __init__(self, wake_time, sleep_time):
        self.wake_time = wake_time
        self.sleep_time = sleep_time

    def are_we_awake(self, current_time):
        if current_time >= self.wake_time and current_time < self.sleep_time:
            return True
        return False
    