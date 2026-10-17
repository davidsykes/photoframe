class ImageDisplayDurationSecondsWrapper:
    def __init__(self,
                 database,
                 default_value):
        self._database = database
        self._value = default_value

    def get(self):
        return self._value

    def set(self, value):
        self._value = value