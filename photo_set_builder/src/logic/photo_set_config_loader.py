from photo_set_builder.src.data.photo_set_configuration import PhotoSetConfiguration


class PhotoSetConfigLoader:
    def __init__(self, config_file_loader):
        self._config_file_loader = config_file_loader

    def load_config(self, config_path):
        config = self._config_file_loader.load_config_file(config_path)

        return PhotoSetConfiguration(
            config.get('include_in_photo_sets'),
            config.get('filter'),
        )