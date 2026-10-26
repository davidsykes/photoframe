from viewer.src.viewer_exit_exception import ViewerExitException

class MenuControl:
    def __init__(self,
                 name,
                 action,
                 *,
                 rect_xywh=None,
                 position=None,
                 size=None):
        self.name = name
        self._rect_xywh = rect_xywh if rect_xywh is not None else position + size
        self._action = action
        if len(self._rect_xywh) != 4:
            raise ViewerExitException(103,f'Control {name} has invalid coordinates {self._rect_xywh}')

    def mouse_down(self, x, y):
        left = self._rect_xywh[0]
        top = self._rect_xywh[1]
        right = left + self._rect_xywh[2] - 1
        bottom = top + self._rect_xywh[3] - 1
        if (x >= left and
            y >= top and
            x <= right and
            y <= bottom):
            return self.activate()

    def activate(self):
        return self._action()
