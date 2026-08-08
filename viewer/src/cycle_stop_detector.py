class CycleStopDetector:
    def __init__(self, reasons):
        self._reasons = reasons
        self._stop = False

    def check_for_stop(self):
        for reason in self._reasons:
            if reason.check_for_stop():
                self._stop = True
                return True
        return False
