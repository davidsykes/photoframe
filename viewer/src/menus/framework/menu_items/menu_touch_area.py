
from viewer.src.menus.framework.menu_items.menu_control import MenuControl


class MenuTouchArea(MenuControl):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
    
    def render(self, display):
        pass
