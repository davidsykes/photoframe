class ActionStatusResultStatusUpdater:
    def __init__(self, status_updater, system_operations):
        self._status_updater = status_updater
        self._system_operations = system_operations

    def record_status(self, description, status):
        update_time = self._system_operations.get_current_time_of_day(
            ).isoformat(timespec='minutes')
        self._status_updater.update_status(
            description,
            f'{status} {update_time}'
        )