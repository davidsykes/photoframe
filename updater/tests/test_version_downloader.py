import unittest
from unittest.mock import Mock

from updater.src.version_downloader import VersionDownloader


class VersionDownloaderTests(unittest.TestCase):
    def test_the_version_is_downloaded(self):
        self.remote_files_retriever.download_file.return_value = True

        result = self.out.download_version(["name", "url"])

        self.remote_files_retriever.download_file.assert_called_once_with(
            'url','name.zip')

        self.assertTrue(result)

    def test_if_the_download_fails_false_is_returned_and_the_failure_logged(self):
        self.remote_files_retriever.download_file.return_value = False

        result = self.out.download_version(["name", "url"])

        self.assertFalse(result)
        self.system_operations.log.assert_called_once_with(
            'Download version name to url failed')

    @classmethod
    def setUp(self):
        self.system_operations = Mock()
        self.remote_files_retriever = Mock()
        self.out = VersionDownloader(
            self.system_operations,
            self.remote_files_retriever)
