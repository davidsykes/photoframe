class SleepTimer:
    def __init__(self, sleep_time, wake_time):
        self.sleep_time = sleep_time
        self.wake_time = wake_time

    def are_we_awake(self):
        raise NotImplementedError("This method should be implemented in a subclass.")
        # now = datetime.now().time()
        # if self.sleep_time < self.wake_time:
        #     return not (self.sleep_time <= now < self.wake_time)
        # else:
        #     return not (now >= self.sleep_time or now < self.wake_time)