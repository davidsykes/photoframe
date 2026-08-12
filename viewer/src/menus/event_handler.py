from viewer.src.viewer_exit_exception import ViewerExitException


class EventHandler:
    def __init__(self):
        pass

    def handle_event(self, event):
        raise ViewerExitException(101, "Quit event received")