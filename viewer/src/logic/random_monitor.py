from typing import List
from viewer.src.data.photo_set import PhotoSet


class RandomMonitor:
    def __init__(self, photo_sets: List[PhotoSet]):
        self._set_names = [photo_set.name for photo_set in photo_sets]
        self._set_weightings = [photo_set.random_weighting for photo_set in photo_sets]
        self._set_count_raw = [0 for _ in photo_sets]

    def photo_set(self, photo_set_index):
        self._photo_set_index = photo_set_index
        self._set_count_raw[photo_set_index] += 1

    def photo(self, photo_index):
        pass

    def show(self):
        pass

    def render(self, status_monitor):
        for index in range(len(self._set_names)):
            status_monitor.update_status(
                f'Set {self._set_names[index]}', f'{self._set_weightings[index]} - {self._set_count_raw[index]}')
