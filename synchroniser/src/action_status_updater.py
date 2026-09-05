class ActionStatusUpdater:
    def __init__(self, action_description, sys_operations):
        self.action_description = action_description
        self.sys_operations = sys_operations

    def update_status(self, status):
        now = self.sys_operations.get_current_time()
        status = 'Success' if status else 'Failure'
        self.sys_operations.log(f'{self.action_description}: {status} {now}')