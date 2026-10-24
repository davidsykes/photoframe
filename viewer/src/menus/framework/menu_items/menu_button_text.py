from viewer.src.menus.framework.menu_items.menu_control import MenuControl


class MenuButtonText(MenuControl):
    def __init__(self, text, alt_name=None, **kwargs):
        self._text = text
        name = alt_name if alt_name is not None else text
        super().__init__(name,
                         **kwargs)

    def render(self, display):
        display.draw_rectangle(
            display.COLOUR_LIGHT,
            self._rect_xywh
        )
        display.wrapper.draw_text(
            self._text,
            (self._rect_xywh[0] + 1,
             self._rect_xywh[1] + 1)
        )
