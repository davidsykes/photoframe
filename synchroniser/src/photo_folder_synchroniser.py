from pathlib import Path


class PhotoFolderSynchroniser:
    def __init__(self,
                 system_operations,
                 remote_folder_downloader,
                 images_folder):
        self._system_operations = system_operations
        self._remote_folder_downloader = remote_folder_downloader
        self._images_folder = Path(images_folder)

    def sync_folder(self, photo_folder):
        images_path = self._images_folder / photo_folder.name
        if self._system_operations.isdir(images_path) == False:
            self._remote_folder_downloader.download_folder(
                photo_folder.url,
                images_path
            )