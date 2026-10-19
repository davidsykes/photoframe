
class MenuButton2:
    def __init__(self, text, action, position, size):
        self._text = text
        self._action = action
        self._position = position
        self._size = size
        self._x = position[0]
        self._y = position[1]
        self._w = size[0]
        self._h = size[1]
        self._x2 = self._x + self._w - 1
        self._y2 = self._y + self._h - 1

    def render(self, display):
        display.draw_rectangle(
            display.COLOUR_LIGHT,
            (self._x,
             self._y,
             self._w,
             self._h)
        )
        display.draw_text(
            self._text,
            display.COLOUR_WHITE,
            (self._x + 1, self._y + 1)
        )

    def mouse_down(self, x, y):
        if (x >= self._x and
            y >= self._y and
            x <= self._x2 and
            y <= self._y2):
            return self.press()

    def press(self):
        return self._action()
