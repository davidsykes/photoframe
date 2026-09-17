class PhotoSetSelector:
    def __init__(self, randomiser, photo_sets, random_monitor):
        self._randomiser = randomiser
        self._photo_sets = photo_sets
        self.calculate_values(photo_sets)
        self._random_monitor = random_monitor

    def select_photo_set(self):
        index = self._randomiser.choices(
            self._indices,
            self._weights
        )
        self._random_monitor.photo_set(index)
        return self._photo_sets[index]

    def calculate_values(self, photo_sets):
        self._indices = []
        self._weights = []
        count = 0
        for photo_set in photo_sets:
            self._indices.append(count)
            self._weights.append(photo_set.random_weighting)
            count += 1