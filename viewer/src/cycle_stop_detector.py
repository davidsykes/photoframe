class CycleStopDetector:
    def __init__(self):
        self._stop = False

    def should_stop(self):
        return self._stop

    def stop(self):
        self._stop = True