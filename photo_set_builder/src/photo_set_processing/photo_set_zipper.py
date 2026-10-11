class PhotoSetZipper:
    def __init__(self, zipper_implementation):
        self._zipper_implementation = zipper_implementation

    def zip_photo_set(self, set_name, compressed_photos_path):
        print(f'SDAJSADSD {set_name} {compressed_photos_path}')
        zip_name = set_name + '.zip'
        self._zipper_implementation.zip(
            zip_name,
            compressed_photos_path
        )