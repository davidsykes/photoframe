from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.menu_button import MenuButton
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class SettingsMenu(PhotoFrameMenu):
    def __init__(self, menu_navigator):
        buttons = [
            MenuButton(UIConstants.BUTTON_RIGHT,
                       UIConstants.MENU_MARGIN,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       'Back', self.back_action),
            MenuButton(UIConstants.LONG_BUTTON_LEFT,
                       UIConstants.MENU_MARGIN,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       'Set Wake Time', self.set_wake_time_action)
        ]
        PhotoFrameMenu.__init__(self, buttons)

        self._menu_navigator = menu_navigator
        self.is_image_enabled = False

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def back_action(self):
        self.menu_action = MenuAction.BACK

    def set_wake_time_action(self):
        self._menu_navigator.push_wake_time_modifier()