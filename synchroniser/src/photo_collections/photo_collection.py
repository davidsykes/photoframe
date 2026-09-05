class PhotoCollection:
    def __init__(self, photo_collection_raw):
        self.name = photo_collection_raw[0]
        self.url = photo_collection_raw[1]
        self.filter_tags = photo_collection_raw[0]

