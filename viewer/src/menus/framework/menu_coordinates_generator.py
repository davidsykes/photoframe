from viewer.src.menus.framework.ui_constants import UIConstants


class MenuCoordinatesGenerator:
    def wide(self, y):
        return (UIConstants.LONG_BUTTON_LEFT,
                y,
                UIConstants.LONG_BUTTON_WIDTH,
                UIConstants.BUTTON_HEIGHT
        )