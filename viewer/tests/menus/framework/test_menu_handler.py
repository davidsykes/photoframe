import unittest
from unittest.mock import Mock, call

from common.src.system_operations import SystemOperations
from viewer.src.display.display_on_off_controller import DisplayOnOffController
from viewer.src.menus.definitions.debug_menu import DebugMenu
from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.menu_handler import MenuHandler


class MenuHandlerTests(unittest.TestCase):
    def test_a_mouse_down_enables_the_main_menu(self):
        self.out.mouse_down(100,200)
        self.out.mouse_down(101,201)
        self.out.mouse_down(102,202)

        self.main_menu.mouse_down.assert_has_calls(
            [call(101,201),call(102,202)]
        )

    def test_enabling_menu_initialises_main_menu(self):
        self.out.mouse_down(100,200)

        self.main_menu.on_enter.assert_called_once()

    def test_if_mouse_down_returns_BACK_the_menu_is_disabled(self):
        self.out.mouse_down(100,200)
        self.main_menu.mouse_down.side_effect = [MenuAction.BACK, None]
        self.out.mouse_down(101,201)
        self.out.mouse_down(102,202)
        self.out.mouse_down(103,203)

        self.main_menu.mouse_down.assert_has_calls(
            [call(101,201),call(103,203)]
        )

    def test_if_mouse_down_returns_BACK_the_main_menu_is_exited(self):
        self.out.mouse_down(100,200)
        self.main_menu.on_exit.assert_not_called()

        self.main_menu.mouse_down.side_effect = [MenuAction.BACK, None]
        self.out.mouse_down(101,201)
        self.main_menu.on_exit.assert_called_once()

    def test_alternative_menus_can_be_set(self):
        self.out.mouse_down(100,200)
        self.out.mouse_down(101,201)
        self.out.set_current_menu(self.menu_2)
        self.out.mouse_down(102,202)
        self.out.mouse_down(103,203)

        self.main_menu.mouse_down.assert_has_calls(
            [call(101,201)]
        )
        self.menu_2.mouse_down.assert_has_calls(
            [call(102,202),call(103,203)]
        )

    def test_disabling_the_menu_restarts_the_sequnce(self):
        self.out.mouse_down(100,200)
        self.out.mouse_down(101,201)
        self.out.set_current_menu(self.menu_2)
        self.menu_2.mouse_down.side_effect = [MenuAction.BACK, None]
        self.out.mouse_down(102,202)
        self.out.mouse_down(103,203)
        self.out.mouse_down(104,204)

        self.main_menu.mouse_down.assert_has_calls(
            [call(101,201), call(104,204)]
        )
        self.menu_2.mouse_down.assert_has_calls(
            [call(102,202)]
        )

    def test_mouse_downs_are_logged(self):
        self.out.mouse_down(100,200)

        self.system_operations.log.assert_called_once_with(
            'Mouse Down 100 200'
        )

    def test_a_mouse_turns_the_display_on(self):
        self.out.mouse_down(100,200)

        self.display_on_off_controller.display_on.assert_called_once()

    def test_menus_are_rendered_when_they_are_enabled(self):
        self.out.render('display')
        self.main_menu.assert_not_called()

        self.out.mouse_down(100,200)
        self.out.render('display')

        self.main_menu.render.assert_called()

    def setUp(self):
        self.main_menu = Mock()
        self.menu_2 = Mock()
        self.display_on_off_controller = Mock(spec=DisplayOnOffController)
        self.system_operations = Mock(spec=SystemOperations)
        self.out = MenuHandler(
            self.display_on_off_controller,
            self.system_operations)
        self.out.set_main_menu(self.main_menu)
