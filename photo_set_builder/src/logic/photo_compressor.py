class PhotoCompressor:
    def __init__(self, photo_resizer):
        self._photo_resizer = photo_resizer

    def compress_photo(self, photo, compressed_folder_path):
        source = photo.source_path
        destination = compressed_folder_path / photo.photo_name
        self._photo_resizer.resize_photo(
            source,
            destination
        )
