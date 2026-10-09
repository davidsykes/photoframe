from photo_set_builder.src.data.photo_set_configuration import PhotoSetConfiguration
from photo_set_builder.src.logic.photo_set_builder_exception import PhotoSetBuilderException


class PhotoSetConfigLoader:
    def __init__(self, config_file_loader):
        self._config_file_loader = config_file_loader

    def load_config(self, config_path):
        config = self._config_file_loader.load_config_file(config_path)

        if config is None:
            raise PhotoSetBuilderException(f'Could not open config file {config_path}')

        include_in_photo_sets = config.get('include_in_photo_sets')
        if not isinstance(include_in_photo_sets, bool):
            raise PhotoSetBuilderException(f'Invalid include_in_photo_sets value: {config_path}')

        return PhotoSetConfiguration(
            include_in_photo_sets,
            config.get('filter'),
        )