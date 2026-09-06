class WlrRandrCommands:
    def get_display_name_command(self):
        return ['wlr-randr']

    def get_display_on_command(self, display_name):
        return ['wlr-randr', '--output', display_name, '--on']

    def get_display_off_command(self, display_name):
        return ['wlr-randr', '--output', display_name, '--off']