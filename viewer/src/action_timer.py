
class ActionTimer:
    def __init__(self,
                 name,
                 system_operations,
                 action,
                 time_between_checks):
        self._name = name
        self._system_operations = system_operations
        self._action = action
        self._time_between_checks = time_between_checks
        self._next_time = 0

    def run_if_due(self):
        now = self._system_operations.get_time_seconds()
        if now >= self._next_time:
            self._next_time = now + self._time_between_checks
            return self._action()
        return None
