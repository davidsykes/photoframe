
class ViewerVersionsConfigLoader:
    def __init__(self,
                 config_file_updater,
                 config_file_loader,
                 remote_viewer_versions_config_path,
                 local_viewer_versions_config_path):
        self._config_file_updater = config_file_updater
        self._config_file_loader = config_file_loader
        self.remote_viewer_versions_config_path = remote_viewer_versions_config_path
        self.local_viewer_versions_config_path = local_viewer_versions_config_path

    def load_viewer_versions_config(self, viewer_config_remote_url):
        self._config_file_updater.update_config_file(
            viewer_config_remote_url,
            self.local_viewer_versions_config_path)

        new_config = self._config_file_loader.load_config_file(
            self.local_viewer_versions_config_path)
        return new_config
