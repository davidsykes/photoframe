import unittest
from unittest.mock import Mock

from updater.src.version_repeater import VersionRepeater

class VersionRepeaterTests(unittest.TestCase):
    def test_the_version_is_run(self):
        self.out.run_version("name", 22)

        self.version_runner.run_version.assert_called_once_with('name')

    def test_if_the_version_does_not_exist_it_is_downloaded(self):
        self.version_has_been_downloaded_checker.check_if_version_has_been_downloaded.return_value = False

        self.out.run_version("name", 22)

        self.version_downloader.download_version.assert_called_once_with("name")

    def test_if_the_version_already_exists_it_is_not_downloaded(self):
        self.version_has_been_downloaded_checker.check_if_version_has_been_downloaded.return_value = True

        self.out.run_version("name", 22)

        self.version_downloader.download_version.assert_not_called()

    @classmethod
    def setUp(self):
        self.version_runner = Mock()
        self.version_downloader = Mock()
        self.version_has_been_downloaded_checker = Mock()
        self.out = VersionRepeater(
            self.version_has_been_downloaded_checker,
            self.version_downloader,
            self.version_runner)
