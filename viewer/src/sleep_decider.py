class SleepDecider:
    def __init__(self):
        self._awake = True

    def are_we_awake(self):
        return self._awake

    def go_to_sleep(self):
        self._awake = False