import unittest
from datetime import date
from viewer.src.data.remote_config_data import RemoteConfigData
from viewer.src.images.photo_set_date_retriever import PhotoSetDateRetriever

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
        # self.next_image_timer = Mock(spec=ActionTimer)
        # self.image_loader = Mock(spec=ImageLoader)
        # self.image_loader.load_image = self.mock_image_loader_load_image
        # self.awake_decider = Mock()
        # self.awake_decider.are_we_awake.return_value = True
        self.config_data = RemoteConfigData('version', [
            ['Set 1', 'url', 'filter', 'Date 1'],
            ['Set 2', 'url', 'filter', 'Date 2'],
            ['Set 3', 'url', 'filter', 'Date 3'],
        ])
        self.out = PhotoSetDateRetriever()