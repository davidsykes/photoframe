class SequentialPhotoChooser:
    def __init__(self, next_image_timer):
        self._next_image_timer = next_image_timer
        self._cached_photo = None

    def choose_next_photo(self):
        photo = self._next_image_timer.run_if_due()
        if photo is not None:
            self._cached_photo = photo
        return self._cached_photo
