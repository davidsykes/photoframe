class NextImageSelector:
    def __init__(self, randomiser):
        self._randomiser = randomiser
        self._image_count = 0
        self._current_image = 0

    def set_images(self, image_paths):
        self._image_paths = image_paths
        self._image_count = len(image_paths)
        self._current_image = -1

    def select_next_image(self):
        self._current_image += 1
        if self._current_image >= self._image_count:
            self._current_image = 0
        return self._image_paths[self._current_image]