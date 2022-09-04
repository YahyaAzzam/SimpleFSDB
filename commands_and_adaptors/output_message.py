import os
from status import *
from ioutput import IOutput

path = os.path.join(str(os.getcwd()).replace("commands_and_adaptors", ''), "message.json")


class OutputMessage(IOutput):
    def __init__(self, command_name=None, result=None, exception=None):
        self.result = result
        self.status = Status.Success if exception is None else exception.status_code
        self.message = command_name + " is a success" if exception is None else str(exception)

