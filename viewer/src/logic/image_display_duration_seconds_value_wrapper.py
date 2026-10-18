class ImageDisplayDurationSecondsWrapper:
    def __init__(self,
                 database,
                 default_value):
        self._database = database
        self._variable_name = 'image_display_duration_seconds_value'
        self._value = database.get_setting(self._variable_name)
        if self._value is None:
            self._value = default_value

    def get(self):
        return self._value

    def set(self, value):
        self._database.set_setting(self._variable_name, value)
        self._value = value