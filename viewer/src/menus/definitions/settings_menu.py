from viewer.src.menus.framework.menu_action import MenuAction


class SettingsMenu:
    def __init__(self):
        self.is_image_enabled = False

    def on_enter(self):
        pass

    def on_exit(self):
        pass

    def render(self, display):
        pass
        #for button in self._buttons:
        #    button.render(display)

    def mouse_down(self, x, y):
        return None

    def back_action(self):
        self.menu_action = MenuAction.BACK
