
class MenuTouchArea:
    def __init__(self,
                 action,
                 coordinates):
        self._action = action
        self._x = coordinates[0]
        self._y = coordinates[1]
        self._x2 = coordinates[2]
        self._y2 = coordinates[3]

    def mouse_down(self, x, y):
        if (x >= self._x and
            y >= self._y and
            x <= self._x2 and
            y <= self._y2):
            return self.activate()

    def activate(self):
        return self._action()
    
    def render(self, display):
        pass
