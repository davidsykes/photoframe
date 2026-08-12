

class EventsHandler:
    def __init__(self, event_handler):
        self._event_handler = event_handler

    def handle_events(self, events):
        for event in events:
            self._event_handler.handle_event(event)