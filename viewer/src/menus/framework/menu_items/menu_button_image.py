from viewer.src.menus.framework.menu_items.menu_control import MenuControl


class MenuButtonImage(MenuControl):
    def __init__(self,
                 name,
                 image_path,
                 action,
                 **kwargs):
        super().__init__(name, action, **kwargs)
        self._image_path = image_path
        self._image = None

    def render(self, display):
        wrapper = display.wrapper
        if self._image is None:
            self.load_image(wrapper)
        wrapper.show_image(self._image,
                           (self._rect_xywh[0],
                           self._rect_xywh[1]))

    def load_image(self, wrapper):
        self._image = wrapper.load_image_from_file_and_scale(
            self._image_path,
            (self._rect_xywh[2],
             self._rect_xywh[3])
        )