class HistoricPhotoChooser:
    def __init__(self, photo_history):
        self._photo_history = photo_history
        self._current_index = None

    def enable(self):
        self._current_index = 0

    def disable(self):
        self._current_index = None

    def back(self):
        if self._current_index < len(self._photo_history) - 1:
            self._current_index += 1

    def forward(self):
        if self._current_index > 0:
            self._current_index -= 1

    def choose_previous_photo(self):
        if self._current_index is None:
            return None
        return self._photo_history[self._current_index]