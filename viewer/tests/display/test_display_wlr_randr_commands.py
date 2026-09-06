import unittest

from viewer.src.display.wlr_randr_commands import WlrRandrCommands

class WlrRandrCommandsTests(unittest.TestCase):
    def test_get_the_display_name(self):
        command = self.out.get_display_name_command()

        self.assertEqual(
            command, ['wlr-randr'])

    def test_get_display_on_command(self):
        command = self.out.get_display_on_command('DisplayName')

        self.assertEqual(
            command, ['wlr-randr', '--output', 'DisplayName', '--on'])

    def test_get_display_off_command(self):
        command = self.out.get_display_off_command('DisplayName')

        self.assertEqual(
            command, ['wlr-randr', '--output', 'DisplayName', '--off'])

    def setUp(self):
        self.out = WlrRandrCommands()
