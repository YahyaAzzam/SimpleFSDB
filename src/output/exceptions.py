from output.status import *


class NoParameterError(Exception):
    def __init__(self, message):
        self.status_code = Status.NoParameterError.name
        super().__init__(message)


class WrongParameterError(Exception):
    def __init__(self, message):
        self.status_code = Status.WrongParameterError.name
        super().__init__(message)
