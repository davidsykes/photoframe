import unittest
from unittest.mock import Mock

from common.src.action_result_recorder import ActionResultRecorder

class TestActionResultRecorder(unittest.TestCase):
    def test_success_is_logged(self):
        self.out.update_status(True)

        self.recorder.record_status.assert_called_once_with(
            'Status Description', 'Success')

    def test_failure_is_logged(self):
        self.out.update_status(False)

        self.recorder.record_status.assert_called_once_with(
            'Status Description', 'Failure')

    def setUp(self):
        self.recorder = Mock()
        self.out = ActionResultRecorder('Status Description',
                                        self.recorder)
