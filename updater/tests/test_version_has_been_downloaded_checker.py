from pathlib import Path
import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from updater.src.version_has_been_downloaded_checker import VersionHasBeenDownloadedChecker


class VersionHasBeenDownloadedCheckerTests(unittest.TestCase):
    def test_if_the_version_has_been_downloaded_return_true(self):
        self.system_operations.isdir.return_value = True

        result = self.out.check_if_version_has_been_downloaded("name")

        self.assertTrue(result)
        self.system_operations.isdir.assert_called_once_with(
            Path("versions_path/name")
        )

    def test_if_the_version_has_been_downloaded_report_progress(self):
        self.system_operations.isdir.return_value = True

        result = self.out.check_if_version_has_been_downloaded("name")

        self.system_operations.progress.assert_called_once_with(
            "Version name has already been downloaded"
        )

    def test_if_the_version_has_not_been_downloaded_return_false(self):
        self.system_operations.isdir.return_value = False

        result = self.out.check_if_version_has_been_downloaded("name2")

        self.assertFalse(result)
        self.system_operations.isdir.assert_called_once_with(
            Path("versions_path/name2")
        )

    def test_if_the_version_has_not_been_downloaded_report_progress(self):
        self.system_operations.isdir.return_value = False

        result = self.out.check_if_version_has_been_downloaded("name2")

        self.system_operations.progress.assert_called_once_with(
            "Version name2 has not been downloaded"
        )

    @classmethod
    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.out = VersionHasBeenDownloadedChecker(
            self.system_operations,
            "versions_path"
        )
