

class EventsHandler:
    def __init__(self,
                 event_source,
                 event_handler):
        self._event_source = event_source
        self._event_handler = event_handler

    def handle_events(self):
        events = self._event_source.get_events()
        had_events = False
        for event in events:
            self._event_handler.handle_event(event)
            had_events = True
        return had_events