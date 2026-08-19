import unittest
from unittest.mock import Mock

from updater.src.version_downloader import VersionDownloader

class MockSandbox:
    def get_version_zip_path(self, version_name):
        if version_name == 'name':
            return 'zip file location'

    def get_unzip_folder(self, version_name):
        if version_name == 'name':
            return 'temporary zip folder'

    def get_version_folder(self, version_name):
        if version_name == 'name':
            return 'version folder'

class VersionDownloaderTests(unittest.TestCase):
    def test_the_version_is_downloaded_unzipped_and_moved(self):

        result = self.out.download_version(["name", "url"])

        self.remote_files_retriever.download_file_or_return_false.assert_called_once_with(
            'url','zip file location')
        self.unzipper.unzip.assert_called_once_with(
            'zip file location', 'temporary zip folder'
        )
        self.system_operations.delete_file.assert_called_once_with(
            'zip file location'
        )
        self.system_operations.rename.assert_called_once_with(
            'temporary zip folder', 'version folder'
        )
        self.system_operations.shutil_copy.assert_called_once_with(
            'project config file', 'version folder'
        )
        self.assertTrue(result)

    def test_if_the_download_fails_false_is_returned_and_the_failure_logged(self):
        self.remote_files_retriever.download_file_or_return_false.return_value = False

        result = self.out.download_version(["name", "url"])

        self.remote_files_retriever.download_file_or_return_false.assert_called_once_with(
            'url','zip file location')
        self.unzipper.unzip.assert_not_called()
        self.system_operations.delete_file.assert_not_called()
        self.system_operations.rename.assert_not_called()
        self.system_operations.shutil_copy.assert_not_called()
        self.assertFalse(result)
        self.system_operations.error.assert_called_once_with(
            'Download version name to zip file location failed')

    def test_if_the_unzip_fails_false_is_returned_and_the_failure_logged(self):
        self.unzipper.unzip.return_value = False

        result = self.out.download_version(["name", "url"])

        self.remote_files_retriever.download_file_or_return_false.assert_called_once_with(
            'url','zip file location')
        self.unzipper.unzip.assert_called_once_with(
            'zip file location', 'temporary zip folder'
        )
        self.system_operations.delete_file.assert_not_called()
        self.system_operations.rename.assert_not_called()
        self.system_operations.shutil_copy.assert_not_called()
        self.assertFalse(result)
        self.system_operations.error.assert_called_once_with(
            'Unzip folder zip file location failed')

    def test_if_the_move_fails_false_is_returned_and_the_failure_logged(self):
        self.system_operations.rename.return_value = False

        result = self.out.download_version(["name", "url"])

        self.remote_files_retriever.download_file_or_return_false.assert_called_once_with(
            'url','zip file location')
        self.unzipper.unzip.assert_called_once_with(
            'zip file location', 'temporary zip folder'
        )
        self.system_operations.delete_file.assert_called_once_with(
            'zip file location'
        )
        self.system_operations.rename.assert_called_once_with(
            'temporary zip folder', 'version folder'
        )
        self.system_operations.shutil_copy.assert_not_called()
        self.assertFalse(result)
        self.system_operations.error.assert_called_once_with(
            'Move folder temporary zip folder failed')

    @classmethod
    def setUp(self):
        self.system_operations = Mock()
        self.sandbox = MockSandbox()
        self.remote_files_retriever = Mock()
        self.unzipper = Mock()
        self.out = VersionDownloader(
            self.system_operations,
            self.sandbox,
            self.remote_files_retriever,
            self.unzipper,
            'project config file')
