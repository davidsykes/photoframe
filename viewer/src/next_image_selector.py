class NextImageSelector:
    def __init__(self, randomiser):
        self.randomiser = randomiser

    def set_images(self, image_paths):
        self._image_paths = image_paths

    def select_next_image(self):
        return self._image_paths[0]