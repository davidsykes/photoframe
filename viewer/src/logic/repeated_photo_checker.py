class RepeatedPhotoChecker:
    def __init__(self,
                 system_operations,
                 status_updater):
        self._system_operations = system_operations
        self._status_updater = status_updater
        self.shown = {}
        self.photos_shown = 0
        self.minimum_repeat_length = None

    def check_for_repeats(self, photo):
        self.photos_shown += 1
        if photo in self.shown:
            last_shown = self.shown[photo]
            self._system_operations.log(f'RPT {last_shown} {self.photos_shown} {photo}')
            repeat_count = self.photos_shown - last_shown
            self._status_updater.update_status('Repeat minimum', repeat_count)
        self.shown[photo] = self.photos_shown