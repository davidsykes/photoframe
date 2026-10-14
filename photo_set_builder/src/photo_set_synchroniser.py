from photo_set_builder.src.logic.photo_set_builder_exception import PhotoSetBuilderException


class PhotoSetSynchroniser:
    def __init__(self,
                 system_operations,
                 viewer_config_manager,
                 dropbox_path):
        self._system_operations = system_operations
        self._viewer_config_manager = viewer_config_manager
        self._dropbox_path = dropbox_path

    def synchronise_photo_set(self, photo_set):
        self.copy_zip_file(photo_set)
        config_entry = self._viewer_config_manager.find_photo_set_config(
            photo_set.name
        )
        config_entry.update_version()
        config_entry.update_date(str(self._system_operations.get_today()))

    def copy_zip_file(self, photo_set):
        source = photo_set.zip_path
        if source is None:
            raise PhotoSetBuilderException(
                f'Set {photo_set.name} zip path has not been set')
        destination = self._dropbox_path / (photo_set.name + '.zip')
        self._system_operations.shutil_copy(source, destination)
