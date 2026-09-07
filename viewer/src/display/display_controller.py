class DisplayController:
    def __init__(self,
                 subprocess_wrapper,
                 subprocess_command_generator,
                 status_updater,
                 system_operations):
        self._subprocess_wrapper = subprocess_wrapper
        self._subprocess_command_generator = subprocess_command_generator
        self._status_updater = status_updater
        self._system_operations = system_operations

    def initialise(self):
        command = None
        try:
            command = self._subprocess_command_generator.get_display_name_command()
            output = self._subprocess_wrapper.run_return_stdout(command)
            self._display_name = output.split(' ', 1)[0]
            self._status_updater.update_status('Display Name', self._display_name)
        except Exception as e:
            self._system_operations.error(f'Display Controller Initialise Error: {command} {e}')
            self._status_updater.update_status('Display Controller Initialise Error', f'{command} {e}')

    def display_on(self):
        try:
            command = self._subprocess_command_generator.get_display_on_command(self._display_name)
            self._system_operations.log(f'Turn display on: {command}')
            self._subprocess_wrapper.run_return_stdout(command)
        except Exception as e:
            self._system_operations.error('Error: Display On ' + str(e))
            self._status_updater.update_status('ERROR: Display On ', str(e))

    def display_off(self):
        try:
            command = self._subprocess_command_generator.get_display_off_command(self._display_name)
            self._system_operations.log(f'Turn display off: {command}')
            self._subprocess_wrapper.run_return_stdout(command)
        except Exception as e:
            self._system_operations.error('Error: Display Off ' + str(e))
            self._status_updater.update_status('ERROR: Display Off ', str(e))