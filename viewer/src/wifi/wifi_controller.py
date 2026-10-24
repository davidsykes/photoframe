class WiFiController:
    def __init__(self, subprocess_wrapper):
        self._subprocess_wrapper = subprocess_wrapper

    def list_network_connections(self):
        command = ['nmcli', '-t', '-f', 'SSID', 'dev', 'wifi', 'list']
        spots = self._subprocess_wrapper.run_return_stdout(command)
        return spots

    def delete_connection(self, ssid):
        command = ['nmcli',
                   'connection',
                   'delete',
                   ssid
                   ]
        return self._subprocess_wrapper.run_return_stdout(command)

    def connect(self, ssid, password):
        command = ['nmcli',
                   'dev',
                   'wifi',
                   'connect',
                   ssid,
                   'password',
                   password]
        return self._subprocess_wrapper.run_return_stdout(command)