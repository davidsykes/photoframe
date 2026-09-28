class ActionResultLogger:
    def __init__(self, system_operations):
        self._system_operations = system_operations

    def record_status(self, description, status):
        self._system_operations.log(f'{description}: {status}')