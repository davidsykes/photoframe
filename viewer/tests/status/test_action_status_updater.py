import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from viewer.src.status.action_status_updater import ActionStatusUpdater
from viewer.src.status.application_status import ApplicationStatus


class TestActionStatusUpdater(unittest.TestCase):
    def test_success_is_logged(self):
        self.out.update_status(True)

        self.application_status.update_status.assert_called_once_with(
            'Action Name', 'Success Time Now')

    def test_failure_is_logged(self):
        self.out.update_status(False)

        self.application_status.update_status.assert_called_once_with(
            'Action Name', 'Failure Time Now')

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.system_operations.get_current_time.return_value = 'Time Now'
        self.application_status = Mock(spec=ApplicationStatus)
        self.out = ActionStatusUpdater(
            'Action Name',
            self.system_operations,
            self.application_status)
