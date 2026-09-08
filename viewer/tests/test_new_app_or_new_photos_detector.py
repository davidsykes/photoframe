import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from viewer.src.new_app_or_new_photos_detector import NewAppOrNewPhotosDetector
from viewer.src.remote_config_version_loader import RemoteConfigVersionLoader
from viewer.src.viewer_exit_exception import ViewerExitException

class NewAppOrNewPhotosDetectorTests(unittest.TestCase):
    def test_nothing_happens_until_the_version_changes(self):
        self.out.poll()
        self.out.poll()
        self.out.poll()
        self.out.poll()

        self.remote_config_version_loader.get_version.return_value = '4.5.6'
        with self.assertRaises(ViewerExitException) as context:
            self.out.poll()
        self.assertEqual(str(context.exception),
                         "100 -> Version changed from 1.2.3 to 4.5.6.")

    def test_version_data_is_logged(self):
        self.out.poll()
        self.system_operations.log.assert_called_once_with(
            'Remote configuration version: 1.2.3. Local version: None'
        )
        self.system_operations.log.reset_mock()
        self.out.poll()
        self.system_operations.log.assert_called_once_with(
            'Remote configuration version: 1.2.3. Local version: 1.2.3'
        )

        self.system_operations.log.reset_mock()
        self.remote_config_version_loader.get_version.return_value = '4.5.6'
        with self.assertRaises(ViewerExitException) as context:
            self.out.poll()
        self.assertEqual(str(context.exception),
                         "100 -> Version changed from 1.2.3 to 4.5.6.")
        self.system_operations.log.assert_called_once_with(
            'Remote configuration version: 4.5.6. Local version: 1.2.3'
        )

    def setUp(self):
        self.remote_config_version_loader = Mock(spec=RemoteConfigVersionLoader)
        self.remote_config_version_loader.get_version.return_value = '1.2.3'
        self.system_operations = Mock(spec=SystemOperations)
        self.out = NewAppOrNewPhotosDetector(
            self.remote_config_version_loader,
            self.system_operations)