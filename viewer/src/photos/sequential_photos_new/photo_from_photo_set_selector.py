class PhotoFromPhotoSetSelectorNew:
    def __init__(self, randomiser):
        self._randomiser = randomiser

    def select_photo(self, photo_set):
        index = self._randomiser.random(len(photo_set.images))
        return photo_set.images[index]