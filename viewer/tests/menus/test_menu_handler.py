import unittest
from unittest.mock import Mock, call

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

    def setUp(self):
        self.main_menu = Mock(spec=MainMenu)
        self.out = MenuHandler(
            self.main_menu)
