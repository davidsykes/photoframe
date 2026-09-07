import unittest
from unittest.mock import Mock, call

from viewer.src.display.display_controller import DisplayController
from viewer.src.menus.main_menu import MainMenu
from viewer.src.menus.menu_handler import MenuHandler


class MenuHandlerTests(unittest.TestCase):
    def test_a_mouse_down_enables_the_main_menu(self):
        self.out.mouse_down(100,200)
        self.out.mouse_down(101,201)
        self.out.mouse_down(102,202)

        self.main_menu.mouse_down.assert_has_calls(
            [call(101,201),call(102,202)]
        )

    def test_a_mouse_turns_the_display_on(self):
        self.out.mouse_down(100,200)

        self.display_controller.display_on.assert_called_once()

    def setUp(self):
        self.main_menu = Mock(spec=MainMenu)
        self.display_controller = Mock(spec=DisplayController)
        self.out = MenuHandler(
            self.main_menu,
            self.display_controller)
