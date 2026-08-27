class PhotoFoldersFilterer:
    def __init__(self, filter_string):
        self._filter_string = filter_string

    def filter_photo_sets(self, unfiltered_photo_folders):
        print(f'Filter photos {unfiltered_photo_folders}')
        return unfiltered_photo_folders