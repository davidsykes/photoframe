class WlopmCommands:
    def get_display_name_command(self):
        return ['wlopm']

    def get_display_on_command(self, display_name):
        return ['wlopm', '--on', display_name]

    def get_display_off_command(self, display_name):
        return ['wlopm', '--off', display_name]