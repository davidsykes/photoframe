import unittest

from viewer.src.image_collection import ImageCollection

class MockSystem:
    def __init__(self, data):
        pass

class ImageCollectionTests(unittest.TestCase):
    def test_images_are_added_and_retrieved_by_id(self):
        collection = ImageCollection()
        collection.add_image(4, "image1.jpg")
        collection.add_image(24, "image2.jpg")
        collection.add_image(14, "image3.jpg")

        self.assertEqual(collection.get_image(4), "image1.jpg")
        self.assertEqual(collection.get_image(24), "image2.jpg")
        self.assertEqual(collection.get_image(14), "image3.jpg")