
class MenuItem:
    def __init__(self, name, coordinates, display_text):
        self.name = name
        self._coordinates = coordinates
    #     self._x = x
    #     self._y = y
    #     self._w = w
    #     self._h = h
    #     self._x2 = x + w - 1
    #     self._y2 = y + h - 1
        self._display_text = display_text
    #     self._action = action

    def render(self, display):
        display.draw_rectangle(
            display.COLOUR_DARK,
            self._coordinates
        )
        display.draw_text(
            self._display_text,
            display.COLOUR_WHITE,
            (self._coordinates[0] + 1,
             self._coordinates[1] + 1)
        )

    # def mouse_down(self, x, y):
    #     if (x >= self._x and
    #         y >= self._y and
    #         x <= self._x2 and
    #         y <= self._y2):
    #         self.press()
    #         return True
    #     return False

    # def press(self):
    #     self._action()
