import unittest
from unittest.mock import Mock
from common.src.config_file import ConfigFile
from common.src.whole_project_configuration import WholeProjectConfiguration
from synchroniser.src.photo_folders_filterer import PhotoFoldersFilterer
from synchroniser.src.photo_folders_remover import PhotoFoldersRemover
from synchroniser.src.photo_folders_synchroniser import PhotoFoldersSynchroniser
from synchroniser.src.remote_config_loader import RemoteConfigLoader
from synchroniser.src.synchroniser_app import SynchroniserApp


class TestSynchroniserApp(unittest.TestCase):
    def test_operation(self):
        self.out.sync()

        self.remote_config_loader.load_config.assert_called_once_with(
            'remote_config_url'
        )
        self.photo_folders_filterer.filter_photo_sets.assert_called_once_with(
            'list of unfiltered photo folders'
        )
        self.photo_folders_synchroniser.sync_folders.assert_called_once_with(
            'list of filtered photo folders'
        )
        self.photo_folders_remover.remove_unreferenced_folders.assert_called_once_with(
            'list of filtered photo folders'
        )

    def setUp(self):
        whole_project_config = Mock(spec = WholeProjectConfiguration)
        whole_project_config.remote_config_url = 'remote_config_url'
        self.remote_config_loader = Mock(RemoteConfigLoader)
        self.remote_config_loader.load_config.return_value = (
            ConfigFile({"photo_folders": 'list of unfiltered photo folders' }, 'test'))
        self.photo_folders_filterer = Mock(PhotoFoldersFilterer)
        self.photo_folders_filterer.filter_photo_sets.return_value = (
            'list of filtered photo folders')
        self.photo_folders_synchroniser = Mock(PhotoFoldersSynchroniser)
        self.photo_folders_remover = Mock(PhotoFoldersRemover)
        self.out = SynchroniserApp(
            whole_project_config,
            self.remote_config_loader,
            self.photo_folders_filterer,
            self.photo_folders_synchroniser,
            self.photo_folders_remover)
