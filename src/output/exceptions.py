# Import necessary modules
import sys
import os

# Append the parent directory of the current file to sys.path
sys.path.append(os.path.dirname(__file__).replace("output", ''))

# Import custom classes and modules
from output.status import *

# Define a custom exception for missing parameters
class NoParameterError(Exception):
    def __init__(self, message):
        # Set the status code for this exception based on your application's status codes
        self.status_code = Status.NoParameterError.name
        super().__init__(message)

# Define a custom exception for incorrect parameters
class WrongParameterError(Exception):
    def __init__(self, message):
        # Set the status code for this exception based on your application's status codes
        self.status_code = Status.WrongParameterError.name
        super().__init__(message)

# Define a custom exception for attempting to overwrite existing data
class OverwriteError(Exception):
    def __init__(self, message):
        # Set the status code for this exception based on your application's status codes
        self.status_code = Status.OverwriteError.name
        super().__init__(message)
