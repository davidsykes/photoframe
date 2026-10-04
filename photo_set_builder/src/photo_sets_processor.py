class PhotoSetsProcessor:
    def __init__(self, photo_set_processor):
        self.photo_set_processor = photo_set_processor

    def process_photo_sets(self, photo_sets):
        for photo_set in photo_sets:
            self.photo_set_processor.process_photo_set(photo_set)