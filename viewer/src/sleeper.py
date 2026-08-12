

class Sleeper:
    def __init__(self,
                 system_operations,
                 sleep_time):
        self._system_operations = system_operations
        self._sleep_time = sleep_time

    def sleep(self):
        time_sec = self._system_operations.time()
        while self._system_operations.time() - time_sec < self._sleep_time:
        #    self._handle_events()
            self._system_operations.sleep(0.1)