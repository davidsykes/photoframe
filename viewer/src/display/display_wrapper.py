class DisplayWrapper:
    def __init__(self, display):
        self._display = display

    def draw_text(self,
                  text,
                  position):
        rendered_text = self._display.render_text(text)
        self._display.draw_rendered_text(
            rendered_text,
            position
        )