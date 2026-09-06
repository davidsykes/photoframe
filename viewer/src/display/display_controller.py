class DisplayController:
    def __init__(self,
                 subprocess_wrapper,
                 status_updater,
                 system_operations):
        self._subprocess_wrapper = subprocess_wrapper
        self._status_updater = status_updater
        self._system_operations = system_operations

    def initialise(self):
        try:
            output = self._subprocess_wrapper.run_return_stdout(['wlr-randr'])
            self._display_name = output.split(' ', 1)[0]
            self._status_updater.update_status('Display Name', self._display_name)
        except Exception as e:
            self._system_operations.error('Error: wlr-randr ' + str(e))
            self._status_updater.update_status('ERROR: wlr-randr', str(e))

    def display_on(self):
        try:
            self._subprocess_wrapper.run_return_stdout(
                ['wlr-randr', '--output', self._display_name, '--on'])
            self._system_operations.log('Display turned on')
        except Exception as e:
            self._system_operations.error('Error: Display On wlr-randr ' + str(e))
            self._status_updater.update_status('ERROR: Display On wlr-randr', str(e))

    def display_off(self):
        try:
            self._subprocess_wrapper.run_return_stdout(
                ['wlr-randr', '--output', self._display_name, '--off'])
            self._system_operations.log('Display turned off')
        except Exception as e:
            self._system_operations.error('Error: Display Off wlr-randr ' + str(e))
            self._status_updater.update_status('ERROR: Display Off wlr-randr', str(e))