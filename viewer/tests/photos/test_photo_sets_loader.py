from pathlib import Path
import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from viewer.src.data.photo_set import PhotoSet
from viewer.src.data.remote_config_data import RemoteConfigData
from viewer.src.photos.photo_set_date_retriever import PhotoSetDateRetriever
from viewer.src.photos.photo_set_loader import PhotoSetLoader
from viewer.src.photos.photo_sets_loader import PhotoSetsLoader

class PhotoSetsLoaderTests(unittest.TestCase):
    def test_photo_sets_images_paths_are_loaded(self):
        photo_sets = self.out.load_photo_sets(
            self.remote_config_data,
            self.photo_sets_path)

        self.assertEqual(photo_sets,
                         [self.photo_set_1,
                          self.photo_set_2,
                          self.photo_set_3]
        )

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.system_operations.listdir.return_value = [
            'Set 1',
            'Set 2',
            'Set 3',
        ]
        self.photo_set_loader = Mock(PhotoSetLoader)
        self.photo_set_loader.load_photo_set = self.mock_load_photo_set
        self.photo_sets_path = Path('photo sets path')
        self.remote_config_data = RemoteConfigData(
            'version',
            'bla bla')
        self.photo_set_date_retriever = Mock(spec=PhotoSetDateRetriever)
        self.photo_set_date_retriever.get_photo_set_date = self.mock_get_photo_set_date
        self.photo_set_1 = PhotoSet('Set 1', 1)
        self.photo_set_2 = PhotoSet('Set 2', 1)
        self.photo_set_3 = PhotoSet('Set 3', 1)
        self.out = PhotoSetsLoader(
            self.system_operations,
            self.photo_set_loader,
            self.photo_set_date_retriever)

    def mock_load_photo_set(self, set_path, set_date):
        if set_path == self.photo_sets_path / 'Set 1':
            if set_date == 'Set 1 Date':
                return self.photo_set_1
        if set_path == self.photo_sets_path / 'Set 2':
            if set_date == 'Set 2 Date':
                return self.photo_set_2
        if set_path == self.photo_sets_path / 'Set 3':
            if set_date == 'Set 3 Date':
                return self.photo_set_3

    def mock_get_photo_set_date(self, set_name, config):
        return set_name + ' Date'