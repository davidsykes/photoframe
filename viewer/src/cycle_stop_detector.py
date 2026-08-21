class CycleStopDetector:
    def __init__(self, reasons):
        self._reasons = reasons
        self._stop = False

    def poll(self):
        for reason in self._reasons:
            if reason.run_if_due():
                self._stop = True
                return True
        return False
