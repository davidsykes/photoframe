class NextPhotoSelector:
    def __init__(self,
                 photo_set_selector,
                 photo_from_photo_set_selector):
           self._photo_set_selector = photo_set_selector
           self._photo_from_photo_set_selector = photo_from_photo_set_selector

    def select_next_photo(self):
          set = self._photo_set_selector.select_photo_set()
          photo = self._photo_from_photo_set_selector.select_photo(set)
          return photo