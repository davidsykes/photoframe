class ImageProvider:
    def __init__(self,
                 photo_path_provider,
                 image_from_file_loader):
        self._photo_path_provider = photo_path_provider
        self._image_from_file_loader = image_from_file_loader
        self._cached_path = None
        self._cached_image = None

    def fetch_image(self):
        photo_path = self._photo_path_provider.choose_photo()
        if photo_path is None:
            self._cached_path = None
            self._cached_image = None
            return None
        if photo_path == self._cached_path:
            return self._cached_image
        self._cached_path = photo_path
        self._cached_image = self._image_from_file_loader.load_image(photo_path)
        return self._cached_image