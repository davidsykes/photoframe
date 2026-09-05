from synchroniser.src.photo_collections.photo_collection import PhotoCollection

class PhotoCollections:
    def __init__(self):
        self.photo_collections = []

    def initialise(self, photo_folders_raw):
        self.photo_collections = [PhotoCollection(photo_collection_raw) for photo_collection_raw in photo_folders_raw]

    def filter_photo_sets(self, photo_folders_filter):
        self.photo_collections = [
            photo_collection for photo_collection in self.photo_collections if photo_folders_filter in photo_collection.filter_tags]

    def __iter__(self):
        for photo_collection in self.photo_collections:
            yield photo_collection

    def list(self, description):
        print(f'PhotoCollections: {description}')
        for photo_collection in self.photo_collections:
            print(f'  {photo_collection.name}')