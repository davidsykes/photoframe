from viewer.src.data.photo_set import PhotoSet


class PhotoSetLoader:
    def __init__(self,
                 system_operations,
                 random_weighter,
                 excluded_extensions):
        self._system_operations = system_operations
        self._random_weighter = random_weighter
        self._excluded_extensions = excluded_extensions

    def load_photo_set(self,
                       photo_set_path,
                       photo_set_date):
        images = self._system_operations.list_files_recursive(
            photo_set_path,
            self._excluded_extensions)
        weight = self._random_weighter.weigh(photo_set_date)
        set = PhotoSet(images, weight)
        return set