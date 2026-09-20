from collections import deque


class PhotoHistory:
    def __init__(self, maximum_count):
        self._history = deque(maxlen = maximum_count)

    def __len__(self) -> int:
        return len(self._history)
    
    def __getitem__(self, index):
        return self._history[-index-1]

    def new_photo(self, photo):
        self._history.append(photo)

    def has_photo_been_shown_recently(self, photo):
        if photo in self._history:
            return True
        return False