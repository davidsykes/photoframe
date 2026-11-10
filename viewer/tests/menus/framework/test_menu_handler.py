import unittest
from unittest.mock import Mock, call

from common.src.system_operations import SystemOperations
from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.menu_handler import MenuHandler
from viewer.src.photos.historic_photo_chooser import HistoricPhotoChooser


class MenuHandlerTests(unittest.TestCase):
    def test_mouse_down_initialises_main_menu_and_subsequent_mouse_downs_are_forwarded(self):
        self.out.mouse_down(100,200)
        self.out.mouse_down(101,201)
        self.out.mouse_down(102,202)

        self.main_menu.mouse_down.assert_has_calls(
            [call(101,201),call(102,202)]
        )

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
        self.main_menu.mouse_down.side_effect = [MenuAction.BACK, None]
        self.out.mouse_down(101,201)

        self.historic_photo_chooser.disable.assert_called_once()

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

    def test_disabling_the_menu_restarts_the_sequence(self):
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

    def test_menus_are_rendered_when_they_are_enabled(self):
        self.out.render('display')
        self.main_menu.assert_not_called()

        self.out.mouse_down(100,200)
        self.out.render('display')

        self.main_menu.render.assert_called()

    def test_when_a_menu_is_enabled_historic_photos_are_enabled(self):
        self.out.set_current_menu(self.main_menu)

        self.historic_photo_chooser.enable.assert_called_once()

    def test_when_menus_are_disabled_historic_photos_are_disabled(self):
        self.out.set_current_menu(self.main_menu)

        self.out.set_current_menu(None)

        self.historic_photo_chooser.enable.assert_called_once()
        self.historic_photo_chooser.disable.assert_called_once()

    def setUp(self):
        self.main_menu = Mock()
        self.menu_2 = Mock()
        self.system_operations = Mock(spec=SystemOperations)
        self.historic_photo_chooser = Mock(spec=HistoricPhotoChooser)
        self.out = MenuHandler(
            self.system_operations,
            self.historic_photo_chooser)
        self.out.set_main_menu(self.main_menu)
