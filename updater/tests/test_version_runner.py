import unittest
from unittest.mock import Mock, call

from updater.src.version_runner import VersionRunner

class MockSandbox:
    def get_version_folder(self, name):
        return 'version rease folder'

class VersionRunnerTests(unittest.TestCase):
    def test_the_updater_is_run_then_the_viewer_is_run(self):
        self.out.run_version('version name')

        self.subprocess_exec.launch_app.assert_has_calls(
            [call(
                'version rease folder',
                'synchroniser.synchroniser_main',
                '',
                3
            ), call(
                'version rease folder',
                'viewer.viewer_app',
                'viewer parameters',
                10
            )]
        )

    @classmethod
    def setUp(self):
        self.system_operations = Mock()
        self.subprocess_exec = Mock()
        self.sandbox = MockSandbox()
        self.version_has_been_downloaded_checker = Mock()
        self.out = VersionRunner(
            self.system_operations,
            self.subprocess_exec,
            self.sandbox,
            'viewer parameters')
