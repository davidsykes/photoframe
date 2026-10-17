from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.menu_items.menu_button import MenuButton
from viewer.src.menus.framework.menu_coordinates_generator import MenuCoordinatesGenerator
from viewer.src.menus.framework.menu_items.display_menu_item import DisplayMenuItem
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class IntegerValueModifierMenu(PhotoFrameMenu):
    def __init__(self):
        mc = MenuCoordinatesGenerator()
        self._title =  DisplayMenuItem('title_text',
                                       mc.wide(10),
                                       '----------')
        self._value_display = DisplayMenuItem('value_display_text',
                                             mc.button(30, 35),
                                             '--')
        buttons = [
            self._title,
            self._value_display,
            MenuButton(30,
                       30,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       '+',
                       self.value_up,
                       'value up'),
            MenuButton(30,
                       40,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       '-',
                       self.value_down,
                       'value down'),
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
        self.display_value = 0

    def setup(self, title, getter, setter):
        self._title.update_text(title)
        self.get_value = getter
        self.set_value = setter
        self.update_display_value(getter())

    def update_display_value(self, display_value):
        self.display_value = display_value
        self.update_display_value_text()

    def update_display_value_text(self):
        self._value_display.update_text(
            str(self.display_value)
        )

    def value_up(self):
        self.update_display_value(
            self.display_value + 1)

    def value_down(self):
        if self.display_value > 0:
            self.update_display_value(
                self.display_value - 1)

    def ok(self):
        self.set_value(self.display_value)
        return MenuAction.BACK
