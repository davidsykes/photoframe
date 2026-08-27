
class SynchroniserApp:
    def __init__(self,
                 whole_project_config,
                 remote_config_loader,
                 photo_folders_filterer,
                 photo_folders_synchroniser,
                 photo_folders_remover):
        self._whole_project_config = whole_project_config
        self._remote_config_loader = remote_config_loader
        self._photo_folders_filterer = photo_folders_filterer
        self._photo_folders_synchroniser = photo_folders_synchroniser
        self._photo_folders_remover = photo_folders_remover

    def sync(self):
        remote_config_url = self._whole_project_config.get('remote_config_url')
        remote_config = self._remote_config_loader.load_config(
            remote_config_url
        )
        unfiltered_photo_folders = remote_config.get('photo_folders')
        filtered_photo_folders = self._photo_folders_filterer.filter_photo_sets(
            unfiltered_photo_folders
        )
        self._photo_folders_synchroniser.sync_folders(filtered_photo_folders)
        self._photo_folders_remover.remove_unreferenced_folders(
            filtered_photo_folders
        )