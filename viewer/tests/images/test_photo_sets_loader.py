import unittest

from viewer.src.images.photo_sets_loader import PhotoSetsLoader

class PhotoSetsLoaderTests(unittest.TestCase):
    def test_photo_sets_images_paths_are_loaded(self):

        photo_sets = self.out.load_image_sets('photo sets path')

        self.assertEqual(photo_sets,
                         [PhotoSet(1),
                          PhotoSet(2),
                          PhotoSet(3)]
        )

    def setUp(self):
        #self.next_image_timer = Mock(spec=ActionTimer)
        self.out = PhotoSetsLoader()
