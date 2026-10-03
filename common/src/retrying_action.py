class RetryingAction:
    def __init__(self,
                 action,
                 sys_operations,
                 action_description,
                 timeout_seconds,
                 retry_interval_seconds):
        self._action = action
        self._sys_operations = sys_operations
        self._action_description = action_description
        self._timeout_seconds = timeout_seconds
        self._retry_interval_seconds = retry_interval_seconds

    def execute(self, *args, **kwargs):
        deadline = self._sys_operations.time_monotonic() + self._timeout_seconds

        while True:
            result = self._action(*args, **kwargs)
            if result:
                return True
            if self._sys_operations.time_monotonic() >= deadline:
                    return False
            
            self._sys_operations.sleep(self._retry_interval_seconds)