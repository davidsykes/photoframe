import unittest
from unittest.mock import Mock, call

from viewer.src.status.application_status import ApplicationStatus

class ViewerOpionsLoaderTests(unittest.TestCase):
    def test_status_can_be_updated_and_displayed(self):
        self.out.update_status('State 1', 'Value 1')
        self.out.update_status('State 2', 'Value 2')
        self.out.render(self.display)

        self.display.print.assert_has_calls(
            [call('State 1: Value 1'),
             call('State 2: Value 2')]
        )

    def test_status_includes_a_simple_log(self):
        self.out.update_status('State 1', 'Value 1')
        self.out.log('Something happened')
        self.out.log('Something happened again')
        self.out.render(self.display)

        self.display.print.assert_has_calls(
            [call('State 1: Value 1'),
             call('Something happened'),
             call('Something happened again')]
        )

    @classmethod
    def setUp(self):
        self.display = Mock()
        self.out = ApplicationStatus()
