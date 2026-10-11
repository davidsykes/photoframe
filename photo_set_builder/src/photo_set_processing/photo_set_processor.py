class PhotoSetProcessor:
    def __init__(self,
                 system_operations,
                 photo_scanner,
                 photos_synchroniser,
                 photo_set_zipper,
                 compressed_folder_name):
        self._system_operations = system_operations
        self._photo_scanner = photo_scanner
        self._photos_synchroniser = photos_synchroniser
        self._photo_set_zipper = photo_set_zipper
        self._compressed_folder_name = compressed_folder_name

    def process_photo_set(self, photo_set):
        if photo_set.config.include_in_sets:
            compressed_photos_path = photo_set.photo_set_path / self._compressed_folder_name
            self._process_photo_set(photo_set, compressed_photos_path)
            if photo_set.photo_set_has_changed:
                self._photo_set_zipper.zip_photo_set(
                    photo_set.name,
                    compressed_photos_path)

    def _process_photo_set(self, photo_set, compressed_photos_path):
        print(f"Processing photo set: {photo_set.name} at {photo_set.photo_set_path} {photo_set.config.include_in_sets}")
        photo_definitions = self._photo_scanner.scan(
            photo_set.photo_set_path)
        compressed_photos = self._photo_scanner.scan(
            compressed_photos_path)
        photo_set_has_changed = self._photos_synchroniser.synchronise_photos(
            photo_definitions, compressed_photos, compressed_photos_path)
        photo_set.photo_set_has_changed = photo_set_has_changed