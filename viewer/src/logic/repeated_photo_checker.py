class RepeatedPhotoChecker:
    def __init__(self):
        self.shown = {}
        self.photos_shown = 0

    def check_for_repeats(self, photo):
        self.photos_shown += 1
        if photo in self.shown:
            last_shown = self.shown[photo]
            print(f'SHSHSHSHSHSH {last_shown} {self.photos_shown} {photo}')
        self.shown[photo] = self.photos_shown