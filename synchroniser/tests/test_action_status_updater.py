import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from synchroniser.src.action_status_updater import ActionStatusUpdater


class TestActionStatusUpdater(unittest.TestCase):
    def test_success_is_logged(self):
        self.out.update_status(True)
        self.system_operations.log.assert_called_once_with(
            'Status Description: Success Time Now')

    def test_failure_is_logged(self):
        self.out.update_status(False)
        self.system_operations.log.assert_called_once_with(
            'Status Description: Failure Time Now')

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.system_operations.get_current_time.return_value = 'Time Now'
        self.out = ActionStatusUpdater('Status Description', self.system_operations)
