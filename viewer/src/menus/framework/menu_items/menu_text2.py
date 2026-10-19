from viewer.src.menus.framework.menu_items.menu_item import MenuItem


class MenuText2(MenuItem):
    def __init__(self,
                 text,
                 position,
                 font=0):
        self._text = text
        self._position = position
        self._font = font

    def render(self, display):
        display.draw_rectangle(
            display.COLOUR_DARK,
            self._position
        )
        display.draw_text(
            self._text,
            display.COLOUR_WHITE,
            (self._position[0] + 1,
             self._position[1] + 1),
            self._font
        )

    def update_text(self, text):
        self._text = text
