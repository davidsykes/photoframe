class WiFiController:
    def __init__(self, subprocess_wrapper):
        self._subprocess_wrapper = subprocess_wrapper
        self._list_wifi_command = ['nmcli', 'dev', 'wifi', 'list']

    def list_hotspots(self):
        spots = self._subprocess_wrapper.run_return_stdout(
            self._list_wifi_command
        )
        return spots