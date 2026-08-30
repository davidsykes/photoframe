from enum import Enum, auto


class UIEventType(Enum):
    MOUSE_DOWN = auto()


class UIEvent:
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.type} -> {self.x, self.y}'
    def __repr__(self):
        return str(self)