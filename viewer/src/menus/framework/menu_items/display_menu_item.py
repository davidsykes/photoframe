from viewer.src.menus.framework.menu_items.menu_item import MenuItem


class DisplayMenuItem(MenuItem):
    def __init__(self, name, coordinates, display_text):
        self.name = name
        self._coordinates = coordinates
        self._display_text = display_text

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

    def update_text(self, text):
        self._display_text = text
