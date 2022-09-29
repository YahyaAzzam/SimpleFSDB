import sys
import os
sys.path.append(os.path.dirname(__file__).replace("output", ''))
from output.status import *


class OutputMessage:
    def __init__(self, command_name=None, result=None, exception=None):
        self.result = result
        self.status = Status.Success.name if exception is None else exception.status_code
        self.message = command_name + " is a success" if exception is None else str(exception)
