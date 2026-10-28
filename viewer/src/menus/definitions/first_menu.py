from viewer.src.menus.framework.menu_items.menu_button_image import MenuButtonImage
from viewer.src.menus.framework.menu_items.menu_button_text import MenuButtonText
from viewer.src.menus.framework.menu_items.menu_text import MenuText
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
            MenuTouchArea('previous image',
                          action=self.previous_image,
                          rect_xywh=(0,20,40,80)),
            MenuText('<', (UIConstants.MENU_MARGIN, 40)),
            MenuTouchArea('next image',
                          action=self.next_image,
                          rect_xywh=(60,20,100,80)),
            MenuText('>', (70, 40)),
            MenuButtonText('Debug',
                        position=(0,UIConstants.SCREEN_HEIGHT-UIConstants.MENU_MARGIN),
                        size=UIConstants.SMALL_BUTTON_SIZE,
                        action=self.debug_menu),
            MenuButtonImage('Settings',
                            'viewer/src/data/settings.png',
                            self.settings_menu,
                            position=(UIConstants.SCREEN_WIDTH - UIConstants.MENU_MARGIN -UIConstants.MENU_IMAGE_SIZE[0],
                                      UIConstants.SCREEN_HEIGHT - UIConstants.MENU_MARGIN - UIConstants.MENU_IMAGE_SIZE[1]),
                            size = UIConstants.MENU_IMAGE_SIZE),
        ]
        super().__init__(buttons, True)

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
        self._debug_menu_enabled = not self._debug_menu_enabled

    def settings_menu(self):
        self._menu_handler.set_current_menu(self._settings_menu)