from photo_set_builder.src.data.viewer_config_photo_folder_configuration import ViewerConfigPhotoFolderConfiguration
from photo_set_builder.src.logic.photo_set_builder_exception import PhotoSetBuilderException


class ViewerConfigManager:
    def __init__(self,
                 config_file_loader,
                 config_file_path,
                 json_wrapper):
        self._config_file_loader = config_file_loader
        self.config_file_path = config_file_path
        self._json_wrapper = json_wrapper
        self._config_version_name = 'version'
        self._photo_folders_config_name = 'photo_folders'
        self.load_config()
        self._current_version = int(self._config.get(self._config_version_name))
        self._config_has_changed = False

    def load_config(self):
        self._config = self._config_file_loader.load_config_file(
            self.config_file_path
        )
        self._photo_folders = self._config.get(self._photo_folders_config_name)

    def find_photo_set_config(self, photo_set_name):
        for photo_set in self._photo_folders:
            photo_set_config = ViewerConfigPhotoFolderConfiguration(photo_set)
            if photo_set_config.name == photo_set_name:
                return photo_set_config

        raise PhotoSetBuilderException(
            f'Photo set {photo_set_name} not found in viewer config file')

    def mark_as_changed(self):
        self._config_has_changed = True

    def save_viewer_config_if_changed(self):
        if self._config_has_changed:
            self._config.config[self._config_version_name] = self._current_version + 1
            save_path = self.config_file_path
            self._json_wrapper.dumps(save_path, self._config.config)
