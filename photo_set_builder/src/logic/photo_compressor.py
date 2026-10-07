class PhotoCompressor:
    def __init__(self, photo_zipper):
        self._photo_zipper = photo_zipper

    def compress_photo(self, photo, compressed_folder_path):
        source = photo.source_path
        destination = compressed_folder_path / photo.photo_name
        self._photo_zipper.zip_photo(
            source,
            destination
        )
