class NextPhotoToShowCache:
    def __init__(self, next_photo_to_show_timer):
        self._next_photo_to_show_timer = next_photo_to_show_timer

    def choose_next_photo(self):
        raise 'choose_next_photo'