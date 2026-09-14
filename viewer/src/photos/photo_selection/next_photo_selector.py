class NextPhotoSelector:
    def __init__(self,
                 photo_set_selector,
                 photo_from_photo_set_selector,
                 random_monitor):
           self._photo_set_selector = photo_set_selector
           self._photo_from_photo_set_selector = photo_from_photo_set_selector
           self._random_monitor = random_monitor

    def select_next_photo(self):
          photo_set = self._photo_set_selector.select_photo_set()
          photo = self._photo_from_photo_set_selector.select_photo(photo_set)
          self._random_monitor.show()
          return photo