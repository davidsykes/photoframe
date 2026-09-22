class PhotoFromPhotoSetSelector:
    def __init__(self, randomiser, random_monitor):
        self._randomiser = randomiser
        self._random_monitor = random_monitor

    def select_photo(self, photo_set):
        index = self._randomiser.random(len(photo_set.images))
        self._random_monitor.photo_chosen(index)
        return photo_set.images[index]