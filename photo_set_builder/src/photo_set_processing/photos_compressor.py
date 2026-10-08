class PhotosCompressor:
    def __init__(self,
                 photo_compressor):
        self._photo_compressor = photo_compressor

    def compress_photos(self,
                        photo_definitions,
                        compressed_photos,
                        compressed_photos_path):
        photos_have_been_compressed = False
        for photo in photo_definitions:
            if photo.photo_name not in compressed_photos:
                self._photo_compressor.compress_photo(
                    photo,
                    compressed_photos_path
                )
                photos_have_been_compressed = True
            else:
                print(f'Already compressed: {photo.photo_name}')
        return photos_have_been_compressed
