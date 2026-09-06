import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from viewer.src.display.display_controller import DisplayController
from viewer.src.display.subprocess_wrapper import SubprocessWrapper
from viewer.src.status.application_status import ApplicationStatus

class DisplayControllerTests(unittest.TestCase):
    def test_initialise_fetches_the_display_name(self):
        self.out.initialise()

        self.subprocess_wrapper.run_return_stdout.assert_called_once_with(
            ['wlr-randr']
        )
        self.status_updater.update_status.assert_called_with(
            'Display Name', 'DisplayName'
        )

    def test_if_initialise_fails_the_error_is_shown(self):
        self.subprocess_wrapper.run_return_stdout.side_effect = (
            Exception('Error text')
        )
        self.out.initialise()

        self.system_operations.error.assert_called_with(
            'Error: wlr-randr Error text'
        )
        self.status_updater.update_status.assert_called_with(
            'ERROR: wlr-randr', 'Error text'
        )

    def test_display_on_calls_the_subprocess_module(self):
        self.out.initialise()

        self.out.display_on()

        self.subprocess_wrapper.run_return_stdout.assert_called_with(
            ['wlr-randr', '--output', 'DisplayName', '--on']
        )

    def test_display_on_logs_the_event(self):
        self.out.initialise()

        self.out.display_on()

        self.system_operations.log.assert_called_with(
            'Display turned on'
        )

    def test_if_display_on_fails_the_event_is_logged(self):
        self.out.initialise()
        self.subprocess_wrapper.run_return_stdout.side_effect = (
            Exception('Error text')
        )

        self.out.display_on()

        self.system_operations.error.assert_called_with(
            'Error: Display On wlr-randr Error text'
        )

    def test_display_off_calls_the_subprocess_module(self):
        self.out.initialise()

        self.out.display_off()

        self.subprocess_wrapper.run_return_stdout.assert_called_with(
            ['wlr-randr', '--output', 'DisplayName', '--off']
        )

    def test_display_off_logs_the_event(self):
        self.out.initialise()

        self.out.display_off()

        self.system_operations.log.assert_called_with(
            'Display turned off'
        )

    def test_if_display_off_fails_the_event_is_logged(self):
        self.out.initialise()
        self.subprocess_wrapper.run_return_stdout.side_effect = (
            Exception('Error text')
        )

        self.out.display_off()

        self.system_operations.error.assert_called_with(
            'Error: Display Off wlr-randr Error text'
        )

    def setUp(self):
        data = Mock()
        data.stdout = 'DisplayName bla bla\nbla bla'
        self.subprocess_wrapper = Mock(spec=SubprocessWrapper)
        self.subprocess_wrapper.run_return_stdout.return_value = data
        self.status_updater = Mock(spec=ApplicationStatus)
        self.system_operations = Mock(spec=SystemOperations)
        self.out = DisplayController(
            self.subprocess_wrapper,
            self.status_updater,
            self.system_operations
        )
