
class ActionTimer:
    def __init__(self,
                 name,
                 system_operations,
                 action,
                 time_between_checks):
        self._name = name
        self._system_operations = system_operations
        self._action = action

        if callable(time_between_checks):
            self._get_time_between_checks = time_between_checks
        else:
            self._get_time_between_checks = lambda: time_between_checks

        self._last_time = 0
        self._paused = False

    def run_if_due(self):
        if self._paused is False:
            now = self._system_operations.get_time_seconds()
            if now >= self._last_time + self._get_time_between_checks():
                self._last_time = now
                return self._action()
        return None

    def pause(self):
        self._paused = True

    def resume(self):
        self._paused = False
