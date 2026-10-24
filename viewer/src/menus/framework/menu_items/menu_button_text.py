from viewer.src.menus.framework.menu_items.menu_control import MenuControl


class MenuButtonText(MenuControl):
    def __init__(self, text, rect_xywh, action):
        self._text = text
        MenuControl.__init__(self,
                             text,
                             rect_xywh,
                             action)

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
