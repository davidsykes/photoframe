class SequentialPhotoChooser:
    def __init__(self, next_image_timer):
        self._next_image_timer = next_image_timer

    def choose_next_photo(self):
        return self._next_image_timer.run_if_due()
