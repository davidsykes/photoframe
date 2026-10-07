class CompressedPhotosRemover:
    def __init__(self, system_operations):
        self._system_operations = system_operations

    def remove_compressed_photos(self,
                                 compressed_photos,
                                 photos_dictionary,
                                 compressed_photos_path):
        for photo in compressed_photos:
            if photo.photo_name not in photos_dictionary:
                path = compressed_photos_path / photo.photo_name
                self._system_operations.log(
                    f'Delete zipped file {path}')
                #self._system_operations.delete_file(path)