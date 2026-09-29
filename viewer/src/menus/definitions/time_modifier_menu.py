from datetime import time

from viewer.src.menus.framework.menu_button import MenuButton
from viewer.src.menus.framework.menu_coordinates_generator import MenuCoordinatesGenerator
from viewer.src.menus.framework.menu_item import MenuItem
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class TimeModifierMenu(PhotoFrameMenu):
    def __init__(self):
        mc = MenuCoordinatesGenerator()
        buttons = [
            MenuItem('display_text',
                     mc.wide(20),
                     '--:--'),
            MenuButton(20,
                       20,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       '+',
                       self.hour_up,
                       'hour up'),
            MenuButton(30,
                       20,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       '+',
                       self.minute_up,
                       'minute up'),
            MenuButton(20,
                       30,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       '-',
                       self.hour_down,
                       'hour down'),
            MenuButton(30,
                       30,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       '-',
                       self.minute_down,
                       'minute down'),
            MenuButton(25,
                       40,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       'Ok',
                       self.ok)
        ]
        PhotoFrameMenu.__init__(self, buttons, False)
        self.get_value = None
        self.set_value = None
        self.display_time = time(12,0)
        self.display_time_text = '--.--'

    def setup(self, getter, setter):
        self.get_value = getter
        self.set_value = setter
        self.update_display_time(getter())

    def update_display_time(self, display_time):
        self.display_time = display_time
        self.update_display_time_text()

    def update_display_time_text(self):
        self.display_time_text = self.display_time.isoformat(timespec='minutes')

    def hour_up(self):
        if self.display_time.hour < 23:
            self.display_time = time(
                self.display_time.hour + 1,
                self.display_time.minute)

    def minute_up(self):
        if self.display_time.minute < 59:
            self.display_time = time(
                self.display_time.hour,
                self.display_time.minute + 1)

    def hour_down(self):
        if self.display_time.hour > 0:
            self.display_time = time(
                self.display_time.hour - 1,
                self.display_time.minute)

    def minute_down(self):
        if self.display_time.minute > 0:
            self.display_time = time(
                self.display_time.hour,
                self.display_time.minute - 1)

    def ok(self):
        self.set_value(self.display_time)
