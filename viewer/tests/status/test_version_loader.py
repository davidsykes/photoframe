import unittest
from unittest.mock import Mock, call

from viewer.src.status.version_loader import VersionLoader


class VersionLoaderTests(unittest.TestCase):
    def test_missing_files_are_detected(self):
        self.system_operations.load_file.return_value = None

        self.out.load_version_details('missing file')

        self.status.update_status.assert_called_once_with(
            'Version', "File 'missing file' not found"
        )

    def test_the_file_contents_are_used(self):
        self.system_operations.load_file.return_value = 'VERSION Contents'

        self.out.load_version_details('VERSION')

        self.status.update_status.assert_called_once_with(
            'Version', 'VERSION Contents'
        )

    def test_line_feeds_are_changed_to_spaces(self):
        self.system_operations.load_file.return_value = 'VERSION\r\n\nContents\n\r\n'

        self.out.load_version_details('VERSION')

        self.status.update_status.assert_called_once_with(
            'Version', 'VERSION  Contents  '
        )

    @classmethod
    def setUp(self):
        self.system_operations = Mock()
        self.status = Mock()
        self.out = VersionLoader(
            self.system_operations,
            self.status)
