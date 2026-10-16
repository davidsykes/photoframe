import unittest
from unittest.mock import Mock

from viewer.src.menus.definitions.settings_menu import SettingsMenu
from viewer.src.menus.framework.menu_navigator import MenuNavigator
from viewer.src.menus.framework.ui_constants import UIConstants

class SettingsMenuTests(unittest.TestCase):
    def test_the_image_show_time_can_be_selected(self):
        self.out.mouse_down(
            UIConstants.LONG_BUTTON_LEFT,
            40
        )

        self.menu_navigator.push_image_display_duration_second_modifier.assert_called_once()

    def setUp(self):
        self.menu_navigator = Mock(spec=MenuNavigator)
        self.out = SettingsMenu(self.menu_navigator)
