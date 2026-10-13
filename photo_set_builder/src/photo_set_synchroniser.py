from photo_set_builder.src.logic.photo_set_builder_exception import PhotoSetBuilderException


class PhotoSetSynchroniser:
    def __init__(self,
                 system_operations,
                 viewer_config_manager,
                 set_name_on_frame_disk_updater,
                 dropbox_path):
        self._system_operations = system_operations
        self._viewer_config_manager = viewer_config_manager
        self._set_name_on_frame_disk_updater = set_name_on_frame_disk_updater
        self._dropbox_path = dropbox_path

    def synchronise_photo_set(self, photo_set):
        config_entry = self._viewer_config_manager.find_photo_set_config(
            photo_set.name
        )
        self.copy_zip_file(photo_set)
        self.update_set_name_on_frame(config_entry)
        self.update_date(config_entry)

    def copy_zip_file(self, photo_set):
        source = photo_set.zip_path
        if source is None:
            raise PhotoSetBuilderException(
                f'Set {photo_set.name} zip path has not been set')
        destination = self._dropbox_path / (photo_set.name + '.zip')
        self._system_operations.shutil_copy(source, destination)

    def update_set_name_on_frame(self, config_entry):
        config_entry[0] = self._set_name_on_frame_disk_updater.update_name(
            config_entry[0]
        )

    def update_date(self, config_entry):
        config_entry[3] = str(self._system_operations.get_today())