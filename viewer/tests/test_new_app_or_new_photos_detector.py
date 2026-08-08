import unittest
from unittest.mock import Mock, call

from viewer.src.new_app_or_new_photos_detector import NewAppOrNewPhotosDetector
from viewer.src.viewer_exit_exception import ViewerExitException

class NewAppOrNewPhotosDetectorTests(unittest.TestCase):
    def test_nothing_happens_until_the_version_changes(self):
        self.out.check_config_version()
        self.out.check_config_version()
        self.out.check_config_version()
        self.out.check_config_version()

        self.remote_version_loader.get_version.return_value = '4.5.6'
        with self.assertRaises(ViewerExitException) as context:
            self.out.check_config_version()
        self.assertEqual(str(context.exception),
                         "100 -> Version changed from 1.2.3 to 4.5.6.")

    @classmethod
    def setUp(self):
        self.remote_version_loader = Mock()
        self.remote_version_loader.get_version.return_value = '1.2.3'
        self.out = NewAppOrNewPhotosDetector(
            self.remote_version_loader)