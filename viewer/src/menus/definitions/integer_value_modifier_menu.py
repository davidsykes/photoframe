from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.menu_coordinates_generator import MenuCoordinatesGenerator
from viewer.src.menus.framework.menu_items.menu_button_text import MenuButtonText
from viewer.src.menus.framework.menu_items.menu_text import MenuText
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class IntegerValueModifierMenu(PhotoFrameMenu):
    def __init__(self):
        mc = MenuCoordinatesGenerator()
        self._title =  MenuText('----------',
                                mc.wide(10))
        self._value_display = MenuText('--',
                                       mc.button(30, 35))
        buttons = [
            self._title,
            self._value_display,
            MenuButtonText('+',
                           action=self.value_up,
                           rect_xywh=(30,
                                      30,
                                      UIConstants.BUTTON_WIDTH,
                                      UIConstants.BUTTON_HEIGHT),
                            alt_name='value up'
                       ),
            MenuButtonText('-',
                           rect_xywh=(30,
                                      40,
                                      UIConstants.BUTTON_WIDTH,
                                      UIConstants.BUTTON_HEIGHT),
                            action=self.value_down,
                            alt_name='value down'),
            MenuButtonText('Ok',
                           rect_xywh=(30,
                                      50,
                                      UIConstants.BUTTON_WIDTH,
                                      UIConstants.BUTTON_HEIGHT),
                            action=self.ok)
        ]
        super().__init__(buttons, False)
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
