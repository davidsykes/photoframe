class PhotoSetSelectorNonRepeating:
    def __init__(self,
                 photo_set_selector,
                 maximum_consecutive_selections,
                 maximum_selection_attempts):
        self._photo_set_selector = photo_set_selector
        self._maximum_consecutive_selections = maximum_consecutive_selections
        self._maximum_selection_attempts = maximum_selection_attempts
        self._last_photo_set = None
        self._last_set_repeat_count = 0

    def select_photo_set(self):
        for _ in range(self._maximum_selection_attempts):
            photo_set = self._photo_set_selector.select_photo_set()
            if photo_set == self._last_photo_set:
                self._last_set_repeat_count += 1
            else:
                self._last_set_repeat_count = 1
            self._last_photo_set = photo_set
            if self._last_set_repeat_count <= self._maximum_consecutive_selections:
                break
        return photo_set