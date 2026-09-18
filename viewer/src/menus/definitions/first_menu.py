from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.menu_button import MenuButton


class FirstMenu:
    def __init__(self,
                 menu_handler,
                 debug_menu,
                 photo_history):
        self._menu_handler = menu_handler
        self._debug_menu = debug_menu
        self._photo_history = photo_history
        self._buttons = [
            MenuButton(90, 0, 10, 5, 'Back', self.back_action),
            MenuButton(1, 47, 10, 5, 'Previous', self.previous_image),
            MenuButton(90,47, 10, 5, 'Next', self.next_image),
            MenuButton(90,90, 10, 5, 'Debug', self.debug_menu),
        ]

    def on_enter(self):
        self._photo_history.begin()

    def on_exit(self):
        self._photo_history.reset()

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
        self._menu_handler.set_current_menu(self._debug_menu)