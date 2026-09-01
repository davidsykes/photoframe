

class ApplicationStatus:
    def __init__(self):
        self.statuses = {}
        self._logs = []

    def update_status(self, key, value):
        self.statuses[key] = value

    def render(self, display):
        for name, value in self.statuses.items():
            display.print_text(f'{name}: {value}')
        for log in self._logs:
            display.print_text(log)

    def log(self, log):
        self._logs.append(log)