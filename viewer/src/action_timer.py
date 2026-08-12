
class ActionTimer:
    def __init__(self,
                 system_operations,
                 action,
                 time_between_checks):
        self._system_operations = system_operations
        self._action = action
        self._time_between_checks = time_between_checks
        self._next_time = self._system_operations.get_time_seconds() + self._time_between_checks

    def poll(self):
        now = self._system_operations.get_time_seconds()
        if now >= self._next_time:
            self._system_operations.log(f"ActionTimer: Triggering action at {now}, next time will be {self._next_time + self._time_between_checks}")
            self._action()
            self._next_time = now + self._time_between_checks