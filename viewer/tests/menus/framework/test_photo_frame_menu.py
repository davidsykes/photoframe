import unittest
from unittest.mock import Mock

from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants

class PhotoFrameMenuTests(unittest.TestCase):
    def test_a_default_back_button_is_added(self):
        self.out.render(self.display)

        self.display.draw_text.assert_called_once_with(
            'Back', 'white',
            (UIConstants.BUTTON_RIGHT+1,
            UIConstants.MENU_MARGIN+1)
        )

    def test_a_mouse_miss_returns_none(self):
        r = self.out.mouse_down(0,0)

        self.assertIsNone(r)

    def test_default_back_button_returns_back(self):
        r = self.out.mouse_down(UIConstants.BUTTON_RIGHT+1,
            UIConstants.MENU_MARGIN+1)

        self.assertEqual(r, MenuAction.BACK)

    def test_press_returns_value_if_the_button_is_found(self):
        self.assertIsNone(self.out.press('non existant button'))
        self.assertEqual(self.out.press('Back'), MenuAction.BACK)

    def test_on_enter_does_nothing(self):
        self.out.on_enter()

    def test_on_exit_does_nothing(self):
        self.out.on_exit()

    def setUp(self):
        self.display = Mock(COLOUR_WHITE='white')
        self.buttons = []
        self.out = PhotoFrameMenu(self.buttons, False)
