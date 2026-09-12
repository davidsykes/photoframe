class PhotoSetSelectorNonRepeating:
    def __init__(self,
                 photo_set_selector,
                 maximum_set_repeat,
                 maximum_check_limit):
        self._photo_set_selector = photo_set_selector
        self._maximum_set_repeat = maximum_set_repeat
        self._maximum_check_limit = maximum_check_limit
        self._last_photo_set = None
        self._last_set_repeat = 0

    def select_photo_set(self):
        photo_set = self._photo_set_selector.select_photo_set()

        while self._last_set_repeat < self._maximum_check_limit:
            if photo_set == self._last_photo_set:
                self._last_set_repeat += 1
                if self._last_set_repeat < self._maximum_set_repeat:
                    return photo_set
            else:
                self._last_photo_set = photo_set
                self._last_set_repeat = 0
                return photo_set
            photo_set = self._photo_set_selector.select_photo_set()
        return photo_set