import unittest
from unittest.mock import Mock, call

from viewer.src.display.display_wrapper import DisplayWrapper
from viewer.src.menus.framework.menu_items.menu_button_image import MenuButtonImage

class MenuButtonImageTests(unittest.TestCase):
    def test_menu_button_images_are_loaded_and_scaled_on_first_render(self):
        self.display.wrapper.load_image_from_file_and_scale.assert_not_called()

        self.out.render(self.display)

        self.display.wrapper.load_image_from_file_and_scale.assert_called_once_with(
            'image path', (30, 40)
        )

    def test_menu_images_are_rendered(self):
        self.out.render(self.display)

        self.display.wrapper.show_image.assert_called_once_with(
            'image', (10,20))

    def test_menu_images_are_only_loaded_once(self):
        self.out.render(self.display)
        self.out.render(self.display)

        self.display.wrapper.load_image_from_file_and_scale.assert_called_once_with(
            'image path', (30,40))
        self.display.wrapper.show_image.assert_has_calls(
            [call('image', (10,20)),
             call('image', (10,20))]
        )

    def test_menu_mouse_press_calls_action(self):
        self.out.mouse_down(11,21)
        self.assertEqual(1, self.action_count)

    def setUp(self):
        self.display = Mock()
        self.display.wrapper = Mock(spec=DisplayWrapper)
        self.display.wrapper.load_image_from_file_and_scale.return_value = 'image'
        self.action_count = 0
        self.out = MenuButtonImage('settings',
                                   'image path',
                                   self.action,
                                   rect_xywh = (10,20,30,40))

    def action(self):
        self.action_count += 1
        return 'value'
