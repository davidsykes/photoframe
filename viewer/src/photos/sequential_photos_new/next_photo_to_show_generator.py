class NextPhotoToShowGenerator:
    def __init__(self,
                 random_photo_selector,
                 photo_history):
        self._random_photo_selector = random_photo_selector
        self._photo_history = photo_history