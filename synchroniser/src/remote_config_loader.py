from pathlib import Path

class RemoteConfigLoader:
    def __init__(self,
                 working_folder,
                 local_config_name,
                 config_file_updater,
                 config_file_loader):
        self._working_folder = Path(working_folder)
        self._local_config_name = local_config_name
        self._config_file_updater = config_file_updater
        self._config_file_loader = config_file_loader

    def load_config(self, remote_config_url):
        config_path = self._working_folder / (self._local_config_name + '.json')
        self._config_file_updater.update_config_file(
            remote_config_url,
            config_path
        )
        return self._config_file_loader.load_config_file(config_path)