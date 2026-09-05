class ActionStatusUpdater:
    def __init__(self,
                 status_description,
                 system_operations,
                 application_status):
        self._status_description = status_description
        self._system_operations = system_operations
        self._application_status = application_status

    def update_status(self, status):
        now = self._system_operations.get_current_time()
        status_str = 'Success' if status else 'Failure'
        self._application_status.update_status(
            self._status_description, f'{status_str} {now}')