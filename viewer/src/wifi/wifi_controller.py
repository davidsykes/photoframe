class WiFiController:
    def __init__(self, subprocess_wrapper):
        self._subprocess_wrapper = subprocess_wrapper
        self._list_wifi_command = ['nmcli', '-t', '-f', 'SSID', 'dev', 'wifi', 'list']

    def list_network_connections(self):
        spots = self._subprocess_wrapper.run_return_stdout(
            self._list_wifi_command
        )
        return spots

    def delete_connection(self, ssid):
        command = ['nmcli',
                   'connection',
                   'delete',
                   f'"{ssid}"'
                   ]
        return self._subprocess_wrapper.run_return_stdout(command)

    def connect(self, ssid, password):
        command = ['nmcli',
                   'dev',
                   'wifi',
                   'connect',
                   f'"{ssid}"',
                   'password',
                   f'"{password}"']
        return self._subprocess_wrapper.run_return_stdout(command)