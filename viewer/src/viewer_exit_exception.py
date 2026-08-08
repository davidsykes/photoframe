class ViewerExitException(Exception):
    def __init__(self, exit_code, msg):
        self.exit_code = exit_code
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.exit_code} -> {self.msg}'