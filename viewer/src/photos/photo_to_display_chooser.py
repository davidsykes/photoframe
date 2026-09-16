class PhotoToDisplayChooser:
    def __init__(self,
                 awake_decider,
                 historic_photo_chooser,
                 sequential_photo_chooser,
                 image_from_file_loader
                 ):
        self._awake_decider = awake_decider
        self._historic_photo_chooser = historic_photo_chooser
        self._sequential_photo_chooser = sequential_photo_chooser

    def choose_photo(self):
        if not self._awake_decider.are_we_awake():
            return None
        photo = self._historic_photo_chooser.choose_previous_photo()
        if photo is not None:
            return photo
        photo = self._sequential_photo_chooser.choose_next_photo()
        if photo is not None:
            return photo
        return None