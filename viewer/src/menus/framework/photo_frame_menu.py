from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.menu_items.menu_button import MenuButton
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
        for button in self._buttons:
            v = button.mouse_down(x, y)
            if v is not None:
                return v
        return None

    def press(self, button_text):
        for button in self._buttons:
            if button.name == button_text:
                return button.press()

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def back_action(self):
        return MenuAction.BACK
