import sys, os

sys.path.append(os.path.join(str(os.path.dirname(os.getcwd())),  "Querio", "lib"))
# Import the IInputAdaptor class and custom exceptions
from input_adaptors.iadaptor import IInputAdaptor
from output.exceptions import *


# Define a class named ParsedInput that inherits from IInputAdaptor
class ParsedInput(IInputAdaptor):
    def __init__(self, parser):
        # Check if a valid command was entered
        if parser.command == "none" or parser.command is None:
            raise NoParameterError("No command was entered")

        # Convert and store the command in lowercase
        self.command = str(parser.command).lower()

        # Store other input parameters
        self.schema_path = parser.schema_path
        self.database = parser.database
        self.table = parser.table
        self.query = parser.query
