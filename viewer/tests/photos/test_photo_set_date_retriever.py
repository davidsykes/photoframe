import unittest
from viewer.src.data.remote_config_data import RemoteConfigData
from viewer.src.photos.photo_set_date_retriever import PhotoSetDateRetriever

class PhotoSetDateRetrieverTests(unittest.TestCase):
    def test_if_set_and_date_exist_the_date_is_returned(self):
        date = self.out.get_photo_set_date('Set 2', self.config_data)

        self.assertEqual(date, 'Date 2')

    def test_if_the_set_is_missing_a_default_is_returned(self):
        date = self.out.get_photo_set_date('Set 20', self.config_data)

        self.assertEqual(date, date.min)

    def test_if_the_date_is_missing_a_default_is_returned(self):
        self.config_data.photo_folders[1] = ['Set 2', 'url', 'filter']

        date = self.out.get_photo_set_date('Set 2', self.config_data)

        self.assertEqual(date, date.min)

    def setUp(self):
        self.config_data = RemoteConfigData('version', [
            ['Set 1', 'url', 'filter', 'Date 1'],
            ['Set 2', 'url', 'filter', 'Date 2'],
            ['Set 3', 'url', 'filter', 'Date 3'],
        ])
        self.out = PhotoSetDateRetriever()