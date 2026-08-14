class MainMenu:
    def __init__(self, statuses):
        self._statuses = statuses
    
    def render(self, display):
        statuses = self._statuses.statuses
        x = 40
        y = 80
        for key, value in statuses.items():
            s = f'{key}: {value}'
            display.print(x, y, s)
            x += 40
            y += 80

    def mouse_down(self, x, y):
        return None