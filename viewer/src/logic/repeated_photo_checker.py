class RepeatedPhotoChecker:
    def __init__(self, system_operations):
        self._system_operations = system_operations
        self.shown = {}
        self.photos_shown = 0

    def check_for_repeats(self, photo):
        self.photos_shown += 1
        if photo in self.shown:
            last_shown = self.shown[photo]
            self._system_operations.log(f'RPT {last_shown} {self.photos_shown} {photo}')
        else:
            self._system_operations.log(f'NEW {self.photos_shown} {photo}')
        self.shown[photo] = self.photos_shown