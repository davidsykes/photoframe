class PhotoFoldersFilterer:
    def __init__(self, system_operations, filter_string):
        self._system_operations = system_operations
        self._filter_string = filter_string

    def filter_photo_sets(self, unfiltered_photo_folders):
        self._system_operations.log(f'Filter photos {unfiltered_photo_folders}')
        filtered_photo_folders = [
            folder for folder in unfiltered_photo_folders
            if self._filter_string in folder[0]]
        self._system_operations.log(f'Filtered photos {filtered_photo_folders}')
        return filtered_photo_folders