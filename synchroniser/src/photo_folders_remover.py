from pathlib import Path


class PhotoFoldersRemover:
    def __init__(self,
                 system_operations,
                 images_path):
        self._system_operations = system_operations
        self._images_path = Path(images_path)

    def remove_unreferenced_folders(self, filtered_photo_folders):
        current_folders = self._system_operations.listdir(
            self._images_path
        )
        wanted_folders = [folder.name for folder in filtered_photo_folders]
        for folder in current_folders:
            if not folder in wanted_folders:
                self._system_operations.rmtree(self._images_path / folder)
