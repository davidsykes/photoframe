class PhotoSetsSynchroniser:
    def __init__(self, photo_set_synchroniser, viewer_config_manager):
        self._photo_set_synchroniser = photo_set_synchroniser
        self._viewer_config_manager = viewer_config_manager

    def synchronise_photo_sets(self, photo_sets_definitions):
        for photo_set in photo_sets_definitions:
            config_entry = self._viewer_config_manager.find_photo_set_config(
                photo_set.name
            )
            print(f'PHHH NNN1 {photo_set.name}')
            print(f'PHHH NNN2 {photo_set.photo_set_path}')
            print(f'PHHH NNN3 {config_entry}')
            self._photo_set_synchroniser.synchronise_photo_set(
                photo_set, config_entry
            )
