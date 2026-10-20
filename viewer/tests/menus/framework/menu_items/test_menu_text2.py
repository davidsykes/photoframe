import unittest
from unittest.mock import Mock

from viewer.src.display.display_wrapper import DisplayWrapper
from viewer.src.menus.framework.menu_items.menu_text2 import MenuText2

class MenuText2Tests(unittest.TestCase):
    def test_text_is_rendered_with_a_background(self):
        self.out.render(self.display)

        self.display.wrapper.draw_text.assert_called_once_with(
            self.menu_text,
            self.text_position
        )

    def setUp(self):
        self.display = Mock()
        self.display.wrapper = Mock(spec=DisplayWrapper)
        self.menu_text = 'menu text'
        self.text_position = (12,34)
        self.out = MenuText2(self.menu_text,
                             self.text_position)
