from viewer.src.menus.framework.menu_action import MenuAction


class PhotoFrameMenu:
    def __init__(self, buttons):
        self._buttons = buttons

    def render(self, display):
        for button in self._buttons:
            button.render(display)

    def mouse_down(self, x, y):
        self.menu_action = MenuAction.NONE
        for button in self._buttons:
            if button.mouse_down(x, y):
                return self.menu_action
        return self.menu_action
