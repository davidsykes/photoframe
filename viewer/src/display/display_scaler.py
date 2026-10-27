class DisplayScaler:
    def __init__(self, display):
        self._display = display

    def scale(self, xy):
        screen_size = self._display.screen_size()
        x = xy[0] * screen_size[0] / 100
        y = xy[1] * screen_size[1] / 100
        return ((x,y))