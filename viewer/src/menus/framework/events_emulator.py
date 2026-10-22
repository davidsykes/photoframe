from viewer.src.menus.framework.ui_constants import UIConstants
from viewer.src.data.uievent import UIEvent, UIEventType


class EventsEmulator:
    def __init__(self, system_operations):
        self._system_operations = system_operations
        self._next_event = 0
        self._events = []
        self._start_time = system_operations.get_time_seconds()
        self._set_initial_events()

    def _set_initial_events(self):
        self.set_events([
            (0.1, 20, 20),
            (0.2, UIConstants.BUTTON_RIGHT+1, 91),
            (0.3, UIConstants.LONG_BUTTON_LEFT+1, 81),
            (0.4, 11, 41),
            (0.5, 11, 51),
            (0.6, 11, 21),
            ]
        )

    def set_events(self, events):
        self._events = [
            (event[0],
            [UIEvent(UIEventType.MOUSE_DOWN, event[1], event[2])]) for event in events
        ]

    def get_events(self):
        if self._next_event < len(self._events):
            return self._check_next_event()
        return []

    def _check_next_event(self):
        current_time = self._system_operations.get_time_seconds() - self._start_time
        current_event = self._events[self._next_event]
        if current_time >= current_event[0]:
            self._next_event += 1
            self._system_operations.log(f'EVENT {current_event[1]}')
            return current_event[1]
        return []