import unittest
from unittest.mock import Mock

from viewer.src.menus.definitions.integer_value_modifier_menu import IntegerValueModifierMenu

class IntegerValueModifierMenuTests(unittest.TestCase):
    def test_menu_items_are_created(self):
        self.assertEqual(len(self.out._controls), 6)
        self.assertEqual(self.out._controls[0].name, 'title_text')
        self.assertEqual(self.out._controls[1].name, 'value_display_text')
        self.assertEqual(self.out._controls[2].name, 'value up')
        self.assertEqual(self.out._controls[3].name, 'value down')
        self.assertEqual(self.out._controls[4].name, 'Ok')

    def test_menu_items_are_displayed(self):
        self.out.render(self.display)
        self.assertTrue('Value to modify' in self.display.rendered_text)
        self.assertTrue('123' in self.display.rendered_text)
        self.assertTrue('+' in self.display.rendered_text)
        self.assertTrue('-' in self.display.rendered_text)

    def test_display_value_can_be_increased(self):
        self.out.activate_control('value up')

        self.assertEqual(self.out.display_value,
                         124)

    def test_display_value_can_be_decreased(self):
        self.out.activate_control('value down')

        self.assertEqual(self.get_display_value(),
                         '122')

    def test_changing_display_value_does_not_affect_set_value(self):
        self.out.activate_control('value up')
        self.assertEqual(self.value, 123)

        self.out.activate_control('value down')
        self.assertEqual(self.value, 123)

    def test_value_is_updated_when_ok_is_pressed(self):
        self.out.activate_control('value up')
        self.out.activate_control('Ok')

        self.assertEqual(self.value, 124)

    def test_if_get_and_set_not_set_value_display_defaults_to_undefined(self):
        self.out = IntegerValueModifierMenu()

        self.assertEqual(self.get_display_value(), '--')

    def test_if_get_and_set_not_set_value_defaults_internally_to_0(self):
        self.out = IntegerValueModifierMenu()
        self.out.activate_control('value up')
        self.out.activate_control('value up')

        self.assertEqual(self.out.display_value, 2)

    def setUp(self):
        self.display = Mock()
        self.display.rendered_text = {}
        self.display.draw_text = self.draw_text
        self.out = IntegerValueModifierMenu()
        self.value = 123
        self.out.setup('Value to modify', self.get_value, self.set_value)

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_display_value(self):
        return self.out._value_display._display_text

    def draw_text(self, text, colour, coordinates):
        self.display.rendered_text[text] = (colour, coordinates)