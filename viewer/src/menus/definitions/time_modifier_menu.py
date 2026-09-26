from viewer.src.menus.framework.photo_frame_menu import PhotoFrameMenu


class TimeModifierMenu(PhotoFrameMenu):
    def __init__(self):
        buttons = []
        PhotoFrameMenu.__init__(self, buttons, False)