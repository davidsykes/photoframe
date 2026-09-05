class PhotoCollection:
    def __init__(self, photo_collection_raw):
        self.name = photo_collection_raw[0]
        self.url = photo_collection_raw[1]
        if len(photo_collection_raw) > 2:
            self.filter_tags = photo_collection_raw[2]
        else:
            self.filter_tags = photo_collection_raw[0]

