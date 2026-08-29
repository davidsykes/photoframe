from viewer.src.menus.menu_button import MenuButton
from viewer.src.viewer_exit_exception import ViewerExitException


class MainMenu:
    def __init__(self, statuses):
        self._statuses = statuses
        self._buttons = [
            MenuButton(600, 600, 200, 100, 'Quit')
        ]
    
    def render(self, display):
        self._statuses.render(display)
        for button in self._buttons:
            button.render(display)
        display.draw_button()

    def mouse_down(self, x, y):
        raise ViewerExitException(101, f"Quit by mouse down")
        return None