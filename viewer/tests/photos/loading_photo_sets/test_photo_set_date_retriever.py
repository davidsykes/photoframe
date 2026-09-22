import unittest
from viewer.src.data.remote_config_data import RemoteConfigData
from viewer.src.photos.loading_photo_sets.photo_set_date_retriever import PhotoSetDateRetriever

class PhotoSetDateRetrieverTests(unittest.TestCase):
    def test_if_set_and_date_exist_the_date_is_returned(self):
        date = self.out.get_photo_set_date('Set 2', self.photo_folders)

        self.assertEqual(date, date.fromisoformat('2025-04-04'))

    def test_if_the_set_is_missing_a_default_is_returned(self):
        date = self.out.get_photo_set_date('Set 20', self.photo_folders)

        self.assertEqual(date, date.min)

    def test_if_the_date_is_missing_a_default_is_returned(self):
        self.photo_folders[1] = ['Set 2', 'url', 'filter']

        date = self.out.get_photo_set_date('Set 2', self.photo_folders)

        self.assertEqual(date, date.min)

    def setUp(self):
        self.photo_folders = [
            ['Set 1', 'url', 'filter', 'Date 1'],
            ['Set 2', 'url', 'filter', '2025-04-04'],
            ['Set 3', 'url', 'filter', 'Date 3'],
        ]
        self.out = PhotoSetDateRetriever()