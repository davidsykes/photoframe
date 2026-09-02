class ImageProvider:
    def __init__(self,
                 next_image_timer,
                 image_loader,
                 sleep_decider):
        self._next_image_timer = next_image_timer
        self._image_loader = image_loader
        self._sleep_decider = sleep_decider
        self._cached_image = None

    def provide_image(self):
        if not self._sleep_decider.are_we_awake():
            return None
        path = self._next_image_timer.run_if_due()
        if path is None:
            return self._cached_image
        self._cached_image = self._image_loader.load_image(path)
        return self._cached_image