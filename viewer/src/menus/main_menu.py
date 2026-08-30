from viewer.src.menus.menu_action import MenuAction
from viewer.src.menus.menu_button import MenuButton
from viewer.src.viewer_exit_exception import ViewerExitException


class MainMenu:
    def __init__(self, statuses):
        self._statuses = statuses
        self._buttons = [
            MenuButton(1000, 100, 100, 50, 'Back', self.back_action),
            MenuButton(1000, 200, 100, 50, 'Quit', self.terminate)
        ]
    
    def render(self, display):
        self._statuses.render(display)
        for button in self._buttons:
            button.render(display)
        display.draw_button()

    def mouse_down(self, x, y):
        self.menu_action = MenuAction.NONE
        for button in self._buttons:
            if button.mouse_down(x, y):
                return self.menu_action
        return self.menu_action

    def back_action(self):
        self.menu_action = MenuAction.BACK

    def terminate(self):
        raise ViewerExitException(101, f"Quit by mouse down")
