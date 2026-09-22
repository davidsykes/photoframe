class NoPhotosToProvideHandler:
    def __init__(self, project_root):
        self._photo_path = project_root / 'viewer' / 'src' / 'data' / 'no_photos.png'

    def choose_photo(self):
        return self._photo_path