from dataclasses import dataclass
from enum import Enum, auto


class UIEventType(Enum):
    MOUSE_DOWN = auto()


@dataclass(frozen=True)
class UIEvent:
    type: UIEventType
    x: int
    y: int
