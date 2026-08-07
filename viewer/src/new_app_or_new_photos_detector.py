class NewAppOrNewPhotosDetector:
    def __init__(self,
                 config_file_updater,
                 config_file_loader,
                 remote_config_url,
                 local_config_path):
        self._config_file_updater = config_file_updater
        self._config_file_loader = config_file_loader
        self._remote_config_url = remote_config_url
        self._local_config_path = local_config_path

    def should_stop(self) -> None:
        print(f"Checking for updates from {self._remote_config_url} and local config at {self._local_config_path}")
        self._config_file_updater.update_config_file(
            self._remote_config_url,
            self._local_config_path)
        config = self._config_file_loader.load_config_file(
            self._local_config_path)
        version = config.get('version')
        print(f'Version: {version}')
