from typing import Any
from viewer.src.awake_periods.awake_decider import AwakeDecider
from viewer.src.menus.framework.event_handler import EventHandler


class EventsHandler:
    def __init__(self,
                 event_source:Any,
                 event_handler:EventHandler,
                 awake_decider:AwakeDecider):
        self._event_source = event_source
        self._event_handler = event_handler
        self._awake_decider = awake_decider

    def handle_events(self):
        events = self._event_source.get_events()
        if events:
            self._awake_decider.wake_up()
        had_events = False
        for event in events:
            self._event_handler.handle_event(event)
            had_events = True
        return had_events