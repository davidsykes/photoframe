from viewer.src.data.uievent import UIEvent, UIEventType
from viewer.src.menus.framework.menu_handler import MenuHandler
from viewer.src.viewer_exit_exception import ViewerExitException


class EventHandler:
    def __init__(self, menu_handler:MenuHandler):
        self._menu_handler = menu_handler

    def handle_event(self, event:UIEvent):
        if event.type == UIEventType.MOUSE_DOWN:
            self._menu_handler.mouse_down(event.x, event.y)
        else:
            raise ViewerExitException(101, "Quit event received")