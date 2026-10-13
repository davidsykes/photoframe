from pathlib import Path


class PhotosetBuilderConfig:
    def __init__(self,
                 config_file_loader,
                 config_file_path):
        self._config = config_file_loader.load_config_file(
            config_file_path)

    @property
    def photo_sets_path(self):
        return Path(self._config.get('photo_sets_path'))

    @property
    def viewer_config_path(self):
        return Path(self._config.get('viewer_config_path'))

    @property
    def compressed_folder_name(self):
        return self._config.get('compressed_folder_name')

    @property
    def dropbox_path(self):
        return Path(self._config.get('dropbox_path'))