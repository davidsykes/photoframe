from photo_set_builder.src.logic.photo_set_builder_exception import PhotoSetBuilderException


class ViewerConfigManager:
    def __init__(self,
                 config_file_loader,
                 config_file_path):
        self._config_file_loader = config_file_loader
        self.config_file_path = config_file_path
        self.load_config()

    def load_config(self):
        #print(f'MAMMDSDM {self.config_file_path}')

        self._config = self._config_file_loader.load_config_file(
            self.config_file_path
        )
        self._photo_folders = self._config.get('photo_folders')

    def find_photo_set_config(self, photo_set_name):
        for photo_set in self._photo_folders:
            if photo_set[0] == photo_set_name:
                return photo_set

        raise PhotoSetBuilderException(
            f'Photo set {photo_set_name} not found in viewer config file')
