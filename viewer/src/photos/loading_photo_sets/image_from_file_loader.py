
class ImageFromFileLoader:
    def __init__(self, display):
        self._display = display

    def load_image(self, image_path):
        return self._display.load_full_screen_image(image_path)