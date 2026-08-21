

class Sleeper:
    def __init__(self,
                 system_operations,
                 events_handler,
                 sleep_time):
        self._system_operations = system_operations
        self._events_handler = events_handler
        self._sleep_time = sleep_time

    def sleep(self):
        time_sec = self._system_operations.get_time_seconds()
        while self._system_operations.get_time_seconds() - time_sec < self._sleep_time:
            self._handle_events()
            self._system_operations.sleep(0.1)

    def _handle_events(self):
        self._events_handler.handle_events()