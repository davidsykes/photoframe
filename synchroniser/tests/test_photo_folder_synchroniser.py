from pathlib import Path
import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from synchroniser.src.photo_folder_synchroniser import PhotoFolderSynchroniser
from synchroniser.src.remote_folder_downloader_wrapper import RemoteFolderDownloaderWrapper


class TestPhotoFolderSynchroniser(unittest.TestCase):
    def test_new_folders_are_downloaded_and_uncompressed(self):
        self.system_operations.isdir.return_value = False

        self.out.sync_folder(['name','url'])

        self.system_operations.isdir.assert_called_once_with(
            Path('images folder') / 'name'
        )
        self.remote_folder_downloader.download_folder.assert_called_once_with(
            'url',
            Path('images folder') / 'name'
        )

    def test_existing_folders_are_not_downloaded(self):
        self.system_operations.isdir.return_value = True

        self.out.sync_folder(['name','url'])

        self.system_operations.isdir.assert_called_once_with(
            Path('images folder') / 'name'
        )
        self.remote_folder_downloader.download_folder.assert_not_called()

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.remote_folder_downloader = Mock(spec=RemoteFolderDownloaderWrapper)
        self.out = PhotoFolderSynchroniser(
            self.system_operations,
            self.remote_folder_downloader,
            'images folder'
        )
