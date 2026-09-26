from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.menu_button import MenuButton
from viewer.src.menus.framework.ui_constants import UIConstants


class PhotoFrameMenu:
    def __init__(self, buttons, is_image_enabled):
        self._buttons = buttons
        self._buttons.append(
            MenuButton(UIConstants.BUTTON_RIGHT,
                       UIConstants.MENU_MARGIN,
                       UIConstants.BUTTON_WIDTH,
                       UIConstants.BUTTON_HEIGHT,
                       'Back',
                       self.back_action))
        self.is_image_enabled = is_image_enabled

    def render(self, display):
        for button in self._buttons:
            button.render(display)

    def mouse_down(self, x, y):
        self.menu_action = MenuAction.NONE
        for button in self._buttons:
            if button.mouse_down(x, y):
                return self.menu_action
        return self.menu_action

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def back_action(self):
        self.menu_action = MenuAction.BACK
