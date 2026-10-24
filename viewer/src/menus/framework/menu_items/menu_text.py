
class MenuText:
    def __init__(self,
                 text,
                 position,
                 font=0):
        self._text = text
        self._position = position
        self._font = font

    def render(self, display):
        display.wrapper.draw_text(
            self._text,
            self._position
        )

    def update_text(self, text):
        self._text = text
