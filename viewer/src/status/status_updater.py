

class StatusUpdater:
    def __init__(self):
        self.statuses = {}

    def update_status(self, key, value):
        self.statuses[key] = value

    def text(self):
        return '\n'.join(
            f'{name}: {value}'
            for name, value in self._values.items()
        )