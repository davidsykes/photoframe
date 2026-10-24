
class MenuControl:
    def __init__(self, name, rect_xywh, action):
        self.name = name
        self._rect_xywh = rect_xywh
        self._action = action

    def activate(self, x, y):
        left = self._rect_xywh[0]
        top = self._rect_xywh[1]
        right = left + self._rect_xywh[2] - 1
        bottom = top + self._rect_xywh[3] - 1
        if (x >= left and
            y >= top and
            x <= right and
            y <= bottom):
            return self._action()
