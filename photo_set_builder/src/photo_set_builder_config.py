from pathlib import Path


class PhotosetBuilderConfig:
    def __init__(self,
                 config_file_loader,
                 config_file_path):
        self._config = config_file_loader.load_config_file(
            config_file_path)

    @property
    def photo_sets_location(self):
        return Path(self._config.get('photo_sets_location'))