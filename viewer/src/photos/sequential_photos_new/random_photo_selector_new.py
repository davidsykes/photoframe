class RandomPhotoSelectorNew:
    def __init__(self,
                 random_photo_set_selector,
                 photo_from_photo_set_selecter):
         self._random_photo_set_selector = random_photo_set_selector
         self._photo_from_photo_set_selecter = photo_from_photo_set_selecter

    def select_photo(self):
         photo_set = self._random_photo_set_selector.select_photo_set()
         photo = self._photo_from_photo_set_selecter.select_photo(photo_set)
         return photo