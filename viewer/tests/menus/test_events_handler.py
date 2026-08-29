import unittest
from unittest.mock import Mock, call

from viewer.src.menus.event_handler import EventHandler
from viewer.src.menus.events_handler import EventsHandler

class EventsHandlerTests(unittest.TestCase):
    def test_events_are_passed_from_display_to_event_handler(self):
        self.event_source.get_events.return_value = [1,2,3]

        self.out.handle_events()

        self.event_handler.handle_event.assert_has_calls(
            [call(1),
             call(2),
             call(3)
            ]
        )

    def setUp(self):
        self.event_source = Mock()
        self.event_handler = Mock(spec=EventHandler)
        self.out = EventsHandler(
            self.event_source,
            self.event_handler)
