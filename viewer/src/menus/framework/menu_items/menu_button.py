
class MenuButton:
    def __init__(self, x, y, w, h, text, action, alt_name = None):
        self.name = text if alt_name is None else alt_name
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._x2 = x + w - 1
        self._y2 = y + h - 1
        self._text = text
        self._action = action

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
