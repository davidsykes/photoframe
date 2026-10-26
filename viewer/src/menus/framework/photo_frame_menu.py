from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.menu_items.menu_button_text import MenuButtonText
from viewer.src.menus.framework.ui_constants import UIConstants


class PhotoFrameMenu:
    def __init__(self, controls, is_image_enabled):
        self._controls = controls
        self._controls.append(
            MenuButtonText('Back',
                        action=self.back_action,
                        position=(UIConstants.BUTTON_RIGHT,
                         UIConstants.MENU_MARGIN),
                        size=UIConstants.BUTTON_SIZE))
        self.is_image_enabled = is_image_enabled

    def render(self, display):
        for control in self._controls:
            control.render(display)

    def mouse_down(self, x, y):
        for control in self._controls:
            v = control.mouse_down(x, y)
            if v is not None:
                return v
        return None

    def activate_control(self, button_name):
        for control in self._controls:
            if hasattr(control, 'activateX'):
                if control.name == button_name:
                    return control.activateX()

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def back_action(self):
        return MenuAction.BACK
