from viewer.src.menus.menu_action import MenuAction
from viewer.src.menus.menu_button import MenuButton


class FirstMenu:
    def __init__(self):
        self._buttons = [
            MenuButton(90, 0, 10, 5, 'Back', self.back_action),
            MenuButton(5, 47, 10, 5, 'Previous', self.previous_image),
            MenuButton(9, 47, 10, 5, 'Next', self.next_image),
            MenuButton(90, 6, 10, 5, 'Debug', self.debug_menu),
        ]

    def render(self, display):
        for button in self._buttons:
            button.render(display)

    def mouse_down(self, x, y):
        self.menu_action = MenuAction.NONE
        for button in self._buttons:
            if button.mouse_down(x, y):
                return self.menu_action
        return self.menu_action

    def back_action(self):
        self.menu_action = MenuAction.BACK

    def previous_image(self):
        raise 'oops'

    def next_image(self):
        raise 'oops'

    def debug_menu(self):
        raise 'oops'