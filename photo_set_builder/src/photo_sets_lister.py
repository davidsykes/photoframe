from photo_set_builder.src.data.photo_set_definition import PhotoSetDefinition


class PhotoSetsLister:
    def __init__(self, system_operations):
        self._system_operations = system_operations

    def list_photo_sets(self, photo_sets_path):
        self._system_operations.log(f"Listing photo sets from {photo_sets_path}")
        folders = self._system_operations.listdir(photo_sets_path)
        return [
            PhotoSetDefinition(
                name=folder_name,
                path=photo_sets_path / folder_name
            )
            for folder_name in folders
        ]