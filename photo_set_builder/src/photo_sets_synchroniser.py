class PhotoSetsSynchroniser:
    def __init__(self, photo_set_synchroniser):
        self._photo_set_synchroniser = photo_set_synchroniser

    def synchronise_photo_sets(self, photo_sets_definitions):
        for photo_set in photo_sets_definitions:
            if photo_set.photo_set_has_changed:
                self._photo_set_synchroniser.synchronise_photo_set(
                    photo_set
                )
