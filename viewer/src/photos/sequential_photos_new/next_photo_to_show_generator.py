class NextPhotoToShowGenerator:
    def __init__(self,
                 random_photo_selector,
                 photo_history,
                 maximum_selection_attempts):
        self._random_photo_selector = random_photo_selector
        self._photo_history = photo_history
        self._maximum_selection_attempts = maximum_selection_attempts

    def generate_next_photo(self):
        for _ in range(self._maximum_selection_attempts):
            photo = self._random_photo_selector.select_random_photo()
            if not self._photo_history.has_photo_been_shown_recently(
                photo):
                break
        return photo
