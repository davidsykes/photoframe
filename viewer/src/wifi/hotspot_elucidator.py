from viewer.src.data.wifi_networks import WiFiNetworks


class HotSpotElucidator:
    def __init__(self, wifi_controller):
        self._wifi_controller = wifi_controller

    def list_hotspots(self):
        try:
            spots_text = self._wifi_controller.list_hotspots()
            ssids = [line for line in spots_text.splitlines() if line]
            ssids = list(dict.fromkeys(ssids))
            return WiFiNetworks(
                '' if len(ssids) > 0 else 'No Wifi Networks found',
                ssids)
        except Exception as e:
            return WiFiNetworks(
                str(e),
                []
            )
