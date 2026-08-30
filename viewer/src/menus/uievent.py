from enum import auto


class UIEvent:
    
    MouseDown = auto()

    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.type} -> {self.x, self.y}'