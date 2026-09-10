class NextImageSelector:
    def __init__(self,
                 randomiser,
                 photo_sets):
           self._randomiser = randomiser
           self._photo_sets = photo_sets

    def select_next_image(self):
        raise 'boo'
        # self._current_image += 1
        # if self._current_image >= self._image_count:
        #     self._current_image = 0
        # return self._image_paths[self._current_image]