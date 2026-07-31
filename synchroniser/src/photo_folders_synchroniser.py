
class PhotoFoldersSynchroniser:
    def __init__(self, photo_folder_synchroniser):
        self._photo_folder_synchroniser = photo_folder_synchroniser

    def sync_folders(self, photo_folders):
        for folder in photo_folders:
            self._photo_folder_synchroniser.sync_folder(folder)