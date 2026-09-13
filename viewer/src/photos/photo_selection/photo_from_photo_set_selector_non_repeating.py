from collections import deque

class PhotoFromPhotoSetSelectorNonRepeating:
    def __init__(self,
                 photo_from_photo_set_selector,
                 minimum_repeat_delay,
                 maximum_selection_attempts):
        self._photo_from_photo_set_selector = photo_from_photo_set_selector
        self._minimum_repeat_delay = minimum_repeat_delay
        self._maximum_selection_attempts = maximum_selection_attempts
        self._recent_photos = deque(maxlen = minimum_repeat_delay)

    def select_photo(self, photo_set):
        for _ in range(self._maximum_selection_attempts):
            photo = self._photo_from_photo_set_selector.select_photo(photo_set)

            if photo not in self._recent_photos:
                break

        self._recent_photos.append(photo)
        return photo
    