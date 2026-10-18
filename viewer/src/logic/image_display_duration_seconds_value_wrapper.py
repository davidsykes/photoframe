class ImageDisplayDurationSecondsWrapper:
    def __init__(self,
                 database,
                 default_value):
        self._database = database
        self._variable_name = 'image_display_duration_seconds_value'
        self.load_value(default_value)

    def load_value(self, default_value):
        value = self._database.get_setting(self._variable_name)
        if value is not None and value.isdigit():
            self._value = int(value)
        else:
            self._value = default_value

    def get(self):
        return self._value

    def set(self, value):
        self._database.set_setting(self._variable_name, value)
        self._value = value