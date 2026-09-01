class ImageProvider:
    def __init__(self, next_image_timer, image_loader):
        self._next_image_timer = next_image_timer
        self._image_loader = image_loader
        self._cached_image = None

    def provide_image(self):
        path = self._next_image_timer.run_if_due()
        if path is None:
            return self._cached_image
        self._cached_image = self._image_loader.load_image(path)
        return self._cached_image