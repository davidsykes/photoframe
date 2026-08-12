from enum import auto


class UIEvent:
    
    MouseDown = auto()
    PI_DISPLAY_VERSION = auto()

    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y