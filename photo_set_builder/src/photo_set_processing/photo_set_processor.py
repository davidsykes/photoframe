class PhotoSetProcessor:
    def __init__(self,
                 system_operations,
                 photo_scanner,
                 photos_synchroniser,
                 compressed_folder_name):
        self._system_operations = system_operations
        self._photo_scanner = photo_scanner
        self._photos_synchroniser = photos_synchroniser
        self._compressed_folder_name = compressed_folder_name

    def process_photo_set(self, photo_set):
        photo_set_path = photo_set.photo_set_path
        print(f"Processing photo set: {photo_set.name} at {photo_set_path}")
        photo_definitions = self._photo_scanner.scan(
            photo_set_path)
        compressed_photos_path = photo_set_path / self._compressed_folder_name
        compressed_photos = self._photo_scanner.scan(
            compressed_photos_path)
        sync_result = self._photos_synchroniser.synchronise_photos(
            photo_definitions, compressed_photos, compressed_photos_path)
        photo_set.synchronisation_result = sync_result