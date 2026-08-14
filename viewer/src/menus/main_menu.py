class MainMenu:
    def __init__(self, statuses):
        self._statuses = statuses
    
    def render(self, display):
        statuses = self._statuses.statuses
        x = 20
        y = 40
        for key, value in statuses.items():
            s = f'{key}: {value}'
            display.print(x, y, s)

    def mouse_down(self, x, y):
        return None