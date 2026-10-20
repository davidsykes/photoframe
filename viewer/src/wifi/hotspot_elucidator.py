from viewer.src.data.wifi_networks import WiFiNetworks


class HotSpotElucidator:
    def __init__(self, wifi_controller):
        self._wifi_controller = wifi_controller

    def list_hotspots(self):
        networks = []
        try:
            spots_text = self._wifi_controller.list_hotspots()
            print(f'SSPPOOTTSS "{spots_text}"')
            spots_info = spots_text.splitlines()
            for spot in spots_info[1:]:
                networks.append(spot)
            return WiFiNetworks(
                '' if len(networks) > 0 else 'No Wifi Networks found',
                networks)
        except Exception as e:
            return WiFiNetworks(
                str(e),
                networks
            )
