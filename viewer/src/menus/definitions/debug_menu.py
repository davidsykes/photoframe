from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.menu_button import MenuButton
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants
from viewer.src.viewer_exit_exception import ViewerExitException


class DebugMenu(PhotoFrameMenu):
    def __init__(self,
                 statuses,
                 awake_decider,
                 display_on_off_controller,
                 random_monitor,
                 memory_monitor):
        self.button_x = UIConstants.BUTTON_RIGHT
        self.button_y = UIConstants.MENU_MARGIN
        buttons = []
        buttons.append(self.create_button('Sleep', self.sleep))
        buttons.append(self.create_button('Wake', self.wake))
        buttons.append(self.create_button('Random', self.render_random))
        buttons.append(self.create_button('Crash', self.simulate_crash))
        buttons.append(self.create_button('Quit', self.end_program_cleanly))
        PhotoFrameMenu.__init__(self, buttons, True)

        self._statuses = statuses
        self._awake_decider = awake_decider
        self._display_on_off_controller = display_on_off_controller
        self._random_monitor = random_monitor
        self._memory_monitor = memory_monitor

    def create_button(self, text, action):
        button = MenuButton(self.button_x, self.button_y, UIConstants.BUTTON_WIDTH, UIConstants.BUTTON_HEIGHT, text, action)
        self.button_y += UIConstants.BUTTON_HEIGHT + 1
        return button

    def render(self, display):
        self._statuses.render(display)
        PhotoFrameMenu.render(self, display)

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
        self._memory_monitor.check_memory_usage()
