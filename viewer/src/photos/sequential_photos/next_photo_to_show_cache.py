class NextPhotoToShowCache:
    def __init__(self,
                 next_photo_to_show_timer,
                 photo_history):
        self._next_photo_to_show_timer = next_photo_to_show_timer
        self._photo_history = photo_history
        self._photo_cache = None

    def choose_next_photo(self):
        photo = self._next_photo_to_show_timer.run_if_due()
        if photo is not None:
            self._photo_cache = photo
            self._photo_history.new_photo(photo)
        return self._photo_cache