from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.menu_button import MenuButton
from viewer.src.viewer_exit_exception import ViewerExitException


class DebugMenu:
    def __init__(self,
                 statuses,
                 awake_decider,
                 display_on_off_controller,
                 random_monitor):
        self._statuses = statuses
        self._awake_decider = awake_decider
        self._display_on_off_controller = display_on_off_controller
        self._random_monitor = random_monitor
        self._buttons = [
            MenuButton(90, 0, 10, 5, 'Back', self.back_action),
            MenuButton(90, 16, 9, 4, 'Sleep', self.sleep),
            MenuButton(90, 21, 9, 4, 'Wake', self.wake),
            MenuButton(90, 26, 9, 4, 'Random', self.render_random),
            MenuButton(90, 31, 9, 4, 'Crash', self.simulate_crash),
            MenuButton(90, 36, 9, 4, 'Quit', self.end_program_cleanly)
        ]

    def on_enter(self):
        pass

    def on_exit(self):
        pass

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

    def sleep(self):
        self._awake_decider.go_to_sleep()
        self.menu_action = MenuAction.BACK

    def wake(self):
        self._awake_decider.wake_up()
        self.menu_action = MenuAction.BACK

    def end_program_cleanly(self):
        raise ViewerExitException(101, "Quit by mouse down")

    def simulate_crash(self):
        raise ViewerExitException(102, "Crash simulated by mouse down")

    def render_random(self):
        self._random_monitor.render(self._statuses)
