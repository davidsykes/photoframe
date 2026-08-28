from viewer.src.viewer_exit_exception import ViewerExitException


class MainMenu:
    def __init__(self, statuses):
        self._statuses = statuses
    
    def render(self, display):
        self._statuses.render(display)
        # statuses = self._statuses.statuses
        # x = 10
        # y = 20
        # for key, value in statuses.items():
        #     s = f'{key}: {value}'
        #     display.print(x, y, s)
        #     y += 20
        display.draw_button()

    def mouse_down(self, x, y):
        raise ViewerExitException(101, f"Control-C event received")
        return None