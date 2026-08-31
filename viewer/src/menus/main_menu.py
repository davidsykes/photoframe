from viewer.src.menus.menu_action import MenuAction
from viewer.src.menus.menu_button import MenuButton
from viewer.src.viewer_exit_exception import ViewerExitException


class MainMenu:
    def __init__(self, statuses, next_image_timer):
        self._statuses = statuses
        self._next_image_timer = next_image_timer
        self._buttons = [
            MenuButton(924, 50, 100, 50, 'Back', self.back_action),
            MenuButton(924, 120, 100, 50, 'Pause', self.pause),
            MenuButton(924, 170, 100, 50, 'Resume', self.resume),
            MenuButton(924, 220, 100, 50, 'Quit', self.terminate)
        ]
    
    def render(self, display):
        self._statuses.render(display)
        for button in self._buttons:
            button.render(display)

    def mouse_down(self, x, y):
        self.menu_action = MenuAction.NONE
        for button in self._buttons:
            if button.mouse_down(x, y):
                return self.menu_action
        return self.menu_action

    def back_action(self):
        self.menu_action = MenuAction.BACK

    def pause(self):
        self._next_image_timer.pause()

    def resume(self):
        self._next_image_timer.resume()

    def terminate(self):
        raise ViewerExitException(101, f"Quit by mouse down")
