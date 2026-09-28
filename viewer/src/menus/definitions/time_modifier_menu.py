from viewer.src.menus.framework.menu_button import MenuButton
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class TimeModifierMenu(PhotoFrameMenu):
    def __init__(self):
        buttons = [
            MenuButton(20,
                       20,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       '+',
                       self.hour_up,
                       'hour up')
        ]
        PhotoFrameMenu.__init__(self, buttons, False)
        self.get_value = None
        self.set_value = None
        self.display_time = '--.--'

    def setup(self, getter, setter):
        self.get_value = getter
        self.set_value = setter
        self.update_display_time(getter())

    def update_display_time(self, display_time):
        self.display_time = display_time.isoformat(timespec='minutes')

    def hour_up(self):
        pass