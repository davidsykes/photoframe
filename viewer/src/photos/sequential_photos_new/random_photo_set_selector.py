class RandomPhotoSetSelector:
    def __init__(self, randomiser, photo_sets):
        self._randomiser = randomiser
        self._photo_sets = photo_sets
        self.calculate_values(photo_sets)

    def select_photo_set(self):
        index = self._randomiser.choices(
            self._indices,
            self._weights
        )
        return self._photo_sets[index]

    def calculate_values(self, photo_sets):
        self._indices = []
        self._weights = []
        count = 0
        print(f'XXXXXXXXXXXXXXXXXXX {photo_sets}')
        for photo_set in photo_sets:
            self._indices.append(count)
            self._weights.append(photo_set.random_weighting)
            count += 1