

class StatusUpdater:
    def __init__(self):
        self.statuses = {}

    def update_status(self, key, value):
        self.statuses[key] = value
