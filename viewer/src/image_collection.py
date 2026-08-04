
class ImageCollection:
    def __init__(self):
        self._images = {}

    def add_image(self, image_id, image_path):
        self._images[image_id] = image_path

    def get_image(self, image_id):
        return self._images.get(image_id)