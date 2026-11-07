from pathlib import Path

from common.src.config_file_loader import ConfigFileLoader
from photo_set_builder.src.logic.photo_set_builder_exception import PhotoSetBuilderException


class PhotosetBuilderConfig:
    def __init__(self,
                 config_file_loader:ConfigFileLoader,
                 config_file_path:Path):
        self._config = config_file_loader.load_config_file(
            config_file_path)
        if self._config is None:
            raise PhotoSetBuilderException(f'Config file {config_file_path} not found')


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