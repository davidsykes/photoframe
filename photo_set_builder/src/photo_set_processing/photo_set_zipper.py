class PhotoSetZipper:
    def __init__(self, zipper_implementation):
        self._zipper_implementation = zipper_implementation

    def zip_photo_set(self, set_name, compressed_photos_path):
        print(f'Call zipper implementation with {set_name} {compressed_photos_path}')
        return self._zipper_implementation.zip(
            set_name,
            compressed_photos_path
        )