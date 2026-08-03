from pathlib import Path
import unittest
from unittest.mock import Mock

from synchroniser.src.remote_folder_downloader import RemoteFolderDownloader

class RemoteFolderDownloaderTests(unittest.TestCase):
    def test_the_version_is_downloaded_unzipped_and_moved(self):

        result = self.out.download_folder(
            'url',
            'working path',
            'destination path')

        self.remote_files_retriever.download_file.assert_called_once_with(
            'url', Path('working path') / 'zip.zip')
        self.unzipper.unzip.assert_called_once_with(
            Path('working path') / 'zip.zip',
            Path('working path') / 'unzip_folder'
        )
        self.system_operations.delete_file.assert_called_once_with(
            Path('working path') / 'zip.zip'
        )
        self.system_operations.rename.assert_called_once_with(
            Path('working path') / 'unzip_folder', 'destination path'
        )
        self.assertTrue(result)

    def test_if_the_download_fails_false_is_returned_and_the_failure_logged(self):
        self.remote_files_retriever.download_file.return_value = False

        result = self.out.download_folder(
            'url',
            'working path',
            'destination path')

        self.remote_files_retriever.download_file.assert_called_once_with(
            'url', Path('working path') / 'zip.zip')
        self.unzipper.unzip.assert_not_called()
        self.system_operations.delete_file.assert_not_called()
        self.system_operations.rename.assert_not_called()
        self.assertFalse(result)
        self.system_operations.error.assert_called_once_with(
            'Download version url to working path\\zip.zip failed')

    def test_if_the_unzip_fails_false_is_returned_and_the_failure_logged(self):
        self.unzipper.unzip.return_value = False

        result = self.out.download_folder(
            'url',
            'working path',
            'destination path')

        self.remote_files_retriever.download_file.assert_called_once_with(
            'url', Path('working path') / 'zip.zip')
        self.unzipper.unzip.assert_called_once_with(
            Path('working path') / 'zip.zip',
            Path('working path') / 'unzip_folder'
        )
        self.system_operations.delete_file.assert_not_called()
        self.system_operations.rename.assert_not_called()
        self.assertFalse(result)
        self.system_operations.error.assert_called_once_with(
            'Unzip folder working path\\zip.zip failed')

    def test_if_the_move_fails_false_is_returned_and_the_failure_logged(self):
        self.system_operations.rename.return_value = False

        result = self.out.download_folder(
            'url',
            'working path',
            'destination path')

        self.remote_files_retriever.download_file.assert_called_once_with(
            'url', Path('working path') / 'zip.zip')
        self.unzipper.unzip.assert_called_once_with(
            Path('working path') / 'zip.zip',
            Path('working path') / 'unzip_folder'
        )
        self.system_operations.delete_file.assert_called_once_with(
            Path('working path') / 'zip.zip'
        )
        self.system_operations.rename.assert_called_once_with(
            Path('working path') / 'unzip_folder', 'destination path'
        )
        self.assertFalse(result)
        self.system_operations.error.assert_called_once_with(
            'Move folder working path\\unzip_folder to destination path failed')

    @classmethod
    def setUp(self):
        self.system_operations = Mock()
        self.remote_files_retriever = Mock()
        self.unzipper = Mock()
        self.out = RemoteFolderDownloader(
            self.system_operations,
            self.remote_files_retriever,
            self.unzipper
            )
