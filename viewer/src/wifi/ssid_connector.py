from viewer.src.data.wifi_networks import WiFiNetworks

class SSIDConnector:
    def __init__(self, wifi_controller):
        self._wifi_controller = wifi_controller

    def connect(self, ssid, password):
        try:
            self._wifi_controller.delete_connection(ssid)
            return self._wifi_controller.connect(ssid, password)
        except Exception as e:
            return f'Wifi Connect Error: {str(e)}'

