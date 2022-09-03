import json
import os
from status import *
from ioutput import IOutput
path = os.path.join(str(os.getcwd()).replace("commands_and_adaptors", ''), "message.json")


class OutputMessage(IOutput):
    def success(result,  command_character):
        file = open(path, 'r')
        message = json.load(file)
        message["result"] = result
        message["status"] = Status.Success.value
        if command_character == 'c':
            message["message"] = "Success to create database"
        elif command_character == 'g':
            message["message"] = "Success to get the object"
        elif command_character == 's':
            message["message"] = "Success to set the data"
        else:
            message["message"] = "Success to delete the data"
        file = open(path, 'w')
        json.dump(message, file)
        file.close()

    def fail(error_type):
        file = open(path, 'r')
        message = json.load(file)
        message["result"] = None
        if error_type[0] == 'W':
            message["message"] = "Enter the correct parameters"
            message["status"] = Status.WrongParameterError.value
        elif error_type[1] == 'o':
            message["message"] = "No parameters was entered"
            message["status"] = Status.NoParameterError.value
        else:
            message["message"] = "Check the empty parameters"
            message["status"] = Status.NullPointerError.value
        file = open(path, 'w')
        json.dump(message, file)
        file.close()
