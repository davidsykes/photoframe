
class MenuButton:
    def __init__(self, x, y, w, h, text):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._text = text

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
            (self._x, self._y)
        )