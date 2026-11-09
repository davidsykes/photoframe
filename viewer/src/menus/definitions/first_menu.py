from viewer.src.menus.definitions.debug_menu import DebugMenu
from viewer.src.menus.framework.menu_action import MenuAction
from viewer.src.menus.framework.menu_items.menu_button_image import MenuButtonImage
from viewer.src.menus.framework.menu_items.menu_control import MenuControl
from viewer.src.menus.framework.menu_items.menu_text import MenuText
from viewer.src.menus.framework.menu_items.menu_touch_area import MenuTouchArea
from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu
from viewer.src.menus.framework.ui_constants import UIConstants


class FirstMenu(PhotoFrameMenu):
    def __init__(self,
                 menu_handler,
                 settings_menu,
                 debug_menu:DebugMenu,
                 historic_photo_chooser):
        buttons:list[MenuControl|MenuText] = [
            MenuButtonImage('Debug',
                            'viewer/src/data/debug.png',
                           action=self.debug_menu,
                           position=(UIConstants.MENU_MARGIN,
                                     UIConstants.SCREEN_HEIGHT - UIConstants.MENU_MARGIN - UIConstants.MENU_IMAGE_SIZE[1]),
                           size = UIConstants.MENU_IMAGE_SIZE),
            MenuButtonImage('Settings',
                            'viewer/src/data/settings.png',
                            self.settings_menu,
                            position=(UIConstants.SCREEN_WIDTH - UIConstants.MENU_MARGIN -UIConstants.MENU_IMAGE_SIZE[0],
                                      UIConstants.SCREEN_HEIGHT - UIConstants.MENU_MARGIN - UIConstants.MENU_IMAGE_SIZE[1]),
                            size = UIConstants.MENU_IMAGE_SIZE),
            MenuTouchArea('previous image',
                          action=self.previous_image,
                          rect_xywh=(0,10,30,90)),
            MenuText('<', (UIConstants.MENU_MARGIN, 40)),
            MenuTouchArea('next image',
                          action=self.next_image,
                          rect_xywh=(70,10,100,90)),
            MenuText('>', (90, 40)),
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

    def mouse_down(self, x:int, y:int) -> MenuAction | None:
        if self._debug_menu_enabled:
            action = self._debug_menu.mouse_down(x, y)
            if action:
                return action
        return PhotoFrameMenu.mouse_down(self, x, y)

    def previous_image(self):
        self._historic_photo_chooser.back()

    def next_image(self):
        self._historic_photo_chooser.forward()

    def debug_menu(self):
        self._debug_menu_enabled = not self._debug_menu_enabled
        return MenuAction.NONE

    def settings_menu(self):
        self._menu_handler.set_current_menu(self._settings_menu)