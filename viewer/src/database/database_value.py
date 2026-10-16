class DatabaseValue:
    def __init__(self,
                 database,
                 value_name,
                 default_value):
        self._database = database
        self._value_name = value_name

    def get_int(self):
        raise 'boo'