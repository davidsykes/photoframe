class RandomMonitor:
    def __init__(self, photo_sets):
        self._set_counts = [
            [0 for _ in photo_set.images]
            for photo_set in photo_sets
]

    def photo_set(self, photo_set_index):
        self._photo_set_index = photo_set_index

    def photo(self, photo_index):
        self._photo_index = photo_index

    def show(self):
        self._set_counts[self._photo_set_index][self._photo_index] += 1

    def render(self, status_monitor):
        for index, counts in enumerate(self._set_counts):
            text = ' '.join(str(count) for count in counts)
            status_monitor.update_status(f'Set {index}', text)