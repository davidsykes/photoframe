class CycleStopDetector:
    def __init__(self, reasons):
        self._reasons = reasons
        self._stop = False

    def should_stop(self):
        for reason in self._reasons:
            if reason.should_stop():
                self._stop = True
                return True
        return False

    def stop(self):
        self._stop = True