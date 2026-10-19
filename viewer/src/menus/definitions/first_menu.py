from viewer.src.menus.framework.menu_items.menu_button import MenuButton
from viewer.src.menus.framework.menu_items.menu_button2 import MenuButton2
from viewer.src.menus.framework.menu_items.menu_text import MenuText
from viewer.src.menus.framework.menu_items.menu_text2 import MenuText2
from viewer.src.menus.framework.menu_items.menu_touch_area import MenuTouchArea
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class FirstMenu(PhotoFrameMenu):
    def __init__(self,
                 menu_handler,
                 settings_menu,
                 debug_menu,
                 historic_photo_chooser):
        buttons = [
            MenuTouchArea(self.previous_image, (0,20,40,80)),
            MenuText2('<', (UIConstants.MENU_MARGIN, 40)),
            MenuButton(UIConstants.BUTTON_LEFT , 47, UIConstants.BUTTON_WIDTH, UIConstants.BUTTON_HEIGHT, 'Previous', self.previous_image),
            MenuTouchArea(self.next_image, (60,20,100,80)),
            MenuText2('>', (70, 40)),
            MenuButton(UIConstants.BUTTON_RIGHT, 47, UIConstants.BUTTON_WIDTH, UIConstants.BUTTON_HEIGHT, 'Next', self.next_image),
            MenuButton2('Debug',
                        self.debug_menu,
                        (0,UIConstants.SCREEN_HEIGHT-UIConstants.MENU_MARGIN),
                        UIConstants.SMALL_BUTTON_SIZE),
            MenuButton2('Settings',
                        self.settings_menu,
                        (UIConstants.SCREEN_WIDTH - UIConstants.MENU_MARGIN - UIConstants.BUTTON_SIZE[0],
                         UIConstants.SCREEN_WIDTH - UIConstants.MENU_MARGIN - UIConstants.BUTTON_SIZE[1]),
                         UIConstants.BUTTON_SIZE),
        ]
        PhotoFrameMenu.__init__(self, buttons, True)

        self._menu_handler = menu_handler
        self._settings_menu = settings_menu
        self._debug_menu = debug_menu
        self._historic_photo_chooser = historic_photo_chooser
        self._debug_menu_enabled = False

    def on_enter(self):
        self._historic_photo_chooser.enable()

    def on_exit(self):
        self._historic_photo_chooser.disable()

    def render(self, display):
        PhotoFrameMenu.render(self, display)
        if self._debug_menu_enabled:
            self._debug_menu.render(display)

    def mouse_down(self, x, y):
        self.menu_action = PhotoFrameMenu.mouse_down(self, x, y)
        if self._debug_menu_enabled:
            return self._debug_menu.mouse_down(x, y)
        return self.menu_action

    def previous_image(self):
        self._historic_photo_chooser.back()

    def next_image(self):
        self._historic_photo_chooser.forward()

    def debug_menu(self):
        #self._menu_handler.set_current_menu(self._debug_menu)
        self._debug_menu_enabled = not self._debug_menu_enabled

    def settings_menu(self):
        self._menu_handler.set_current_menu(self._settings_menu)