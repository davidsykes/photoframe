from viewer.src.menus.menu_action import MenuAction
from viewer.src.menus.menu_button import MenuButton
from viewer.src.viewer_exit_exception import ViewerExitException


class MainMenu:
    def __init__(self, statuses, next_image_timer, sleep_decider):
        self._statuses = statuses
        self._next_image_timer = next_image_timer
        self._sleep_decider = sleep_decider
        self._buttons = [
            MenuButton(90, 0, 10, 5, 'Back', self.back_action),
            MenuButton(90, 6, 10, 5, 'Pause', self.pause),
            MenuButton(90, 12, 10, 5, 'Resume', self.resume),
            MenuButton(90, 18, 10, 5, 'Sleep', self.sleep),
            MenuButton(90, 24, 10, 5, 'Quit', self.terminate)
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

    def sleep(self):
        self._sleep_decider.go_to_sleep()

    def terminate(self):
        raise ViewerExitException(101, f"Quit by mouse down")
