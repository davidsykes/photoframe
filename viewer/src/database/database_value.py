class DatabaseValue:
    def __init__(self,
                 database,
                 value_name,
                 default_value):
        self._database = database
        self._value_name = value_name
        self._current_value = self.get_database_value(default_value)

    def get_database_value(self, default_value):
        value = self._database.get_setting(self._value_name)
        if value is not None:
            return value
        return default_value

    def get_int(self):
        return int(self._current_value)