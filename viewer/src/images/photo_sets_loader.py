class PhotoSetsLoader:
    def __init__(self,
                 system_operations,
                 photo_set_loader,
                 photo_set_date_retriever):
        self._system_operations = system_operations
        self._photo_set_loader = photo_set_loader
        self._photo_set_date_retriever = photo_set_date_retriever

    def load_photo_sets(self,
                        remote_config_data,
                        photo_sets_path):
        photo_set_folders = self._system_operations.listdir(photo_sets_path)
        photo_sets = []
        for photo_set in photo_set_folders:
            photo_set_path = photo_sets_path / photo_set
            photo_set_date = self._photo_set_date_retriever.get_photo_set_date(
                photo_set,
                remote_config_data)
            photo_set = self._photo_set_loader.load_photo_set(
                photo_set_path,
                photo_set_date
            )
            photo_sets.append(photo_set)
        return photo_sets
