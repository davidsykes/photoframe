

class Sleeper:
    def __init__(self,
                 system_operations,
                 display,
                 event_handler,
                 sleep_time):
        self._system_operations = system_operations
        self._display = display
        self._event_handler = event_handler
        self._sleep_time = sleep_time

    def sleep(self):
        time_sec = self._system_operations.time()
        while self._system_operations.time() - time_sec < self._sleep_time:
            self._handle_events()
            self._system_operations.sleep(0.1)

    def _handle_events(self):
        events = self._display.get_events()
        self._event_handler.handle_events(events)