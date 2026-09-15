import unittest
from viewer.src.data.photo_set import PhotoSet


class PhotoSetTests(unittest.TestCase):
    def test_the_class_holds_name_images_and_weighting(self):
        out = PhotoSet('name', 'images', 'weighting')

        self.assertEqual('name', out.name)
        self.assertEqual('images', out.images)
        self.assertEqual('weighting', out.random_weighting)