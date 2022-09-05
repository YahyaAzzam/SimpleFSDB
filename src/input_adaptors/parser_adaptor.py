from input_adaptors.iadaptor import IInputAdaptor
from output.exceptions import *


class ParsedInput(IInputAdaptor):
    def __init__(self, parser):
        if parser.command == "none" or parser.command is None:
            raise NoParameterError("No command was entered")
        self.command = str(parser.command).lower()
        self.schema = parser.schema
        self.database = parser.database
        self.table = parser.table
        self.primary_key = parser.primary_key
        self.parameter = parser.parameter
        self.value = parser.value
