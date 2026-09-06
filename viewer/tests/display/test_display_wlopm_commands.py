import unittest

from viewer.src.display.wlopm_commands import WlopmCommands

class WlopmCommandsTests(unittest.TestCase):
    def test_get_the_display_name(self):
        command = self.out.get_display_name_command()

        self.assertEqual(
            command, ['wlopm'])

    def test_get_display_on_command(self):
        command = self.out.get_display_on_command('DisplayName')

        self.assertEqual(
            command, ['wlopm', '--on', 'DisplayName'])

    def test_get_display_off_command(self):
        command = self.out.get_display_off_command('DisplayName')

        self.assertEqual(
            command, ['wlopm', '--off', 'DisplayName'])

    def setUp(self):
        self.out = WlopmCommands()
