class HotSpotElucidator:
    def __init__(self, wifi_controller):
        self._wifi_controller = wifi_controller

    def list_hotspots(self):
        spots = self._wifi_controller.list_hotspots()
        print(f'SSPPOOTTSS {spots}')