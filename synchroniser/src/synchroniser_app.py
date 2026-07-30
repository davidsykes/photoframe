
class SynchroniserApp:
    def __init__(self,
                 whole_project_config,
                 remote_config_loader,
                 photo_folders_synchroniser):
        self._whole_project_config = whole_project_config
        self._remote_config_loader = remote_config_loader
        self._photo_folders_synchroniser = photo_folders_synchroniser

    def sync(self):
        remote_config_url = self._whole_project_config['remote_config_url']
        remote_config = self._remote_config_loader.load_config(
            remote_config_url
        )
        photo_folders = remote_config['photo_folders']
        self._photo_folders_synchroniser.sync_folders(photo_folders)