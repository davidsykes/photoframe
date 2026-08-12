

from viewer.src.viewer_exit_exception import ViewerExitException


class EventHandler:
    def __init__(self):
        pass

    def handle_event(self, event):
        print('EventHandler handle_event')
        raise ViewerExitException(100, "Quit event received")