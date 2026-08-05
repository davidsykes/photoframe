class ViewerExitException(Exception):
    def __init__(self, return_code, msg):
        self.return_code = return_code
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.return_code} -> {self.msg}'