class PhotoSetProcessor:
    def __init__(self,
                 system_operations,
                 photo_lister,
                 photos_synchroniser):
        self._system_operations = system_operations
        self._photo_lister = photo_lister
        self._photos_synchroniser = photos_synchroniser

    def process_photo_set(self, photo_set):
        photo_set_path = photo_set.path
        photo_definitions = self._photo_lister.list_photos(
            photo_set_path)
        compressed_photos_path = photo_set_path / 'compressed'
        compressed_photos = self._photo_lister.list_photos(
            compressed_photos_path)
        sync_result = self._photos_synchroniser.synchronise_photos(
            photo_definitions, compressed_photos, compressed_photos_path)
        photo_set.synchronisation_result = sync_result