from datetime import time
from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.menu_items.menu_button import MenuButton
from viewer.src.menus.framework.menu_coordinates_generator import MenuCoordinatesGenerator
from viewer.src.menus.framework.menu_items.display_menu_item import DisplayMenuItem
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class TimeModifierMenu(PhotoFrameMenu):
    def __init__(self):
        mc = MenuCoordinatesGenerator()
        self._title =  DisplayMenuItem('title_text',
                                       mc.wide(10),
                                       '----------')
        self._time_display = DisplayMenuItem('time_display_text',
                                             mc.button(30, 35),
                                             '--:--')
        buttons = [
            self._title,
            self._time_display,
            MenuButton(20,
                       30,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       '+',
                       self.hour_up,
                       'hour up'),
            MenuButton(30,
                       30,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       '+',
                       self.minute_up,
                       'minute up'),
            DisplayMenuItem('hour_text',
                     mc.button(20, 35),
                     'Hour'),
            DisplayMenuItem('minute_text',
                     mc.button(40, 35),
                     'Minute'),
            MenuButton(20,
                       40,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       '-',
                       self.hour_down,
                       'hour down'),
            MenuButton(40,
                       40,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       '-',
                       self.minute_down,
                       'minute down'),
            MenuButton(30,
                       50,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       'Ok',
                       self.ok)
        ]
        PhotoFrameMenu.__init__(self, buttons, False)
        self.get_value = None
        self.set_value = None
        self.display_time = time(12,0)

    def setup(self, title, getter, setter):
        self._title.update_text(title)
        self.get_value = getter
        self.set_value = setter
        self.update_display_time(getter())

    def update_display_time(self, display_time):
        self.display_time = display_time
        self.update_display_time_text()

    def update_display_time_text(self):
        text = self.display_time.isoformat(timespec='minutes')
        self._time_display.update_text(text)

    def hour_up(self):
        if self.display_time.hour < 23:
            self.update_display_time(time(
                self.display_time.hour + 1,
                self.display_time.minute))

    def minute_up(self):
        if self.display_time.minute < 59:
            self.update_display_time(time(
                self.display_time.hour,
                self.display_time.minute + 1))

    def hour_down(self):
        if self.display_time.hour > 0:
            self.update_display_time(time(
                self.display_time.hour - 1,
                self.display_time.minute))

    def minute_down(self):
        if self.display_time.minute > 0:
            self.update_display_time(time(
                self.display_time.hour,
                self.display_time.minute - 1))

    def ok(self):
        self.set_value(self.display_time)
        return MenuAction.BACK
