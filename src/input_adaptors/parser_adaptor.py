import sys
import os
sys.path.append(os.path.dirname(__file__).replace("input_adaptors", ''))
from input_adaptors.iadaptor import IInputAdaptor
from output.exceptions import *


class ParsedInput(IInputAdaptor):
    def __init__(self, parser):
        if parser.command == "none" or parser.command is None:
            raise NoParameterError("No command was entered")
        self.command = str(parser.command).lower()
        self.schema_path = parser.schema_path
        self.database = parser.database
        self.table = parser.table
        self.query = parser.query
