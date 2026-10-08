from photo_set_builder.src.data.photo_set_definition import PhotoSetDefinition


class PhotoSetsLister:
    def __init__(self, system_operations, photo_set_config_loader):
        self._system_operations = system_operations
        self._photo_set_config_loader = photo_set_config_loader

    def list_photo_sets(self, photo_sets_path):
        self._system_operations.log(f"Listing photo sets from {photo_sets_path}")
        folders = self._system_operations.list_sub_directories(photo_sets_path)
        return [
            PhotoSetDefinition(folder_name,
                               photo_sets_path / folder_name,
                               self.load_config(photo_sets_path / folder_name)
            )
            for folder_name in folders
        ]

    def load_config(self, photo_set_path):
        return self._photo_set_config_loader.load_config(
            photo_set_path / 'config.json')