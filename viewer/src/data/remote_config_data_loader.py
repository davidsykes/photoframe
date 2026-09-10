from viewer.src.data.remote_config_data import RemoteConfigData


class RemoteConfigDataLoader:
    def __init__(self,
                 config_file_updater,
                 config_file_loader,
                 status_updater,
                 remote_config_url,
                 local_config_path):
        self._config_file_updater = config_file_updater
        self._config_file_loader = config_file_loader
        self._status_updater = status_updater
        self._remote_config_url = remote_config_url
        self._local_config_path = local_config_path

    def get_config_data(self) -> RemoteConfigData:
        self._config_file_updater.update_config_file(
            self._remote_config_url,
            self._local_config_path)
        config = self._config_file_loader.load_config_file(
            self._local_config_path)
        version = config.get('version')
        photo_folders = config.get('photo_folders')
        print(f'photo_folders = {photo_folders}')
        self._status_updater.update_status('Last Version Check', version)
        return RemoteConfigData(
            version,
            photo_folders
        )
