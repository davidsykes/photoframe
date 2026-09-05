from pathlib import Path
import unittest

from synchroniser.src.photo_collections.photo_collections import PhotoCollections

class TestPhotoCollections(unittest.TestCase):
    def test_collections_can_be_filtered(self):
        self.out.initialise([
            ['set 1 f1', 'url 1'],
            ['set 2 f2', 'url 2'],
            ['set 3 f1', 'url 3'],
            ['set 4 f2', 'url 4']
            ])

        self.out.filter_photo_sets('f2')

        self.assertEqual(
            [photo_collection.name for photo_collection in self.out.photo_collections],
            ['set 2 f2', 'set 4 f2']
        )

    def test_collections_can_be_listed(self):
        self.out.initialise([
            ['set 1 f1', 'url 1'],
            ['set 2 f2', 'url 2'],
            ['set 3 f1', 'url 3'],
            ['set 4 f2', 'url 4']
            ])

        self.assertEqual(
            [photo_collection.name for photo_collection in self.out],
            ['set 1 f1', 'set 2 f2', 'set 3 f1', 'set 4 f2']
        )

    def setUp(self):
        self.out = PhotoCollections()
