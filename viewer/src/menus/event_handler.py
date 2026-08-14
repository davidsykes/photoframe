from viewer.src.viewer_exit_exception import ViewerExitException


class EventHandler:
    def __init__(self, menu_handler):
        self._menu_handler = menu_handler

    def handle_event(self, event):
        if event.type == event.MouseDown:
            self._menu_handler.mouse_down(event.x, event.y)
        else:
            raise ViewerExitException(101, "Quit event received")