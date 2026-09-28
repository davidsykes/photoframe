import unittest
from datetime import time
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from viewer.src.status.action_status_result_status_updater import ActionStatusResultStatusUpdater
from viewer.src.status.application_status import ApplicationStatus


class ActionStatusResultStatusUpdaterTests(unittest.TestCase):
    def test_status_is_update_with_status_and_time(self):
        self.system_operations.get_current_time_of_day.return_value =(
            time.fromisoformat('12:34')
        )

        self.out.record_status('description', 'status')

        self.status_updater.update_status.assert_called_once_with(
            'description',
            'status 12:34'
        )

    def setUp(self):
        self.status_updater = Mock(spec=ApplicationStatus)
        self.system_operations = Mock(spec=SystemOperations)
        self.out = ActionStatusResultStatusUpdater(
            self.status_updater,
            self.system_operations
        )
