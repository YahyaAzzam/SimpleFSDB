import os
import sys
sys.path.append(os.path.join(str(os.getcwd()).replace("commands_and_adaptors", ''), "functions"))
from create_command import *

# from set_command import *
# from get_command import *
# from delete_command import *


class CommandFactory:
    def __init__(self, input_adaptor):
        self.input_adaptor = input_adaptor
        self.validate()
        
    def create(self):
        cmd = str(self.input_adaptor.command).lower()
        if cmd == "create":
            return CreateCommand(self.input_adaptor.schema)
#        elif cmd == "set":
#            return SetCommand(self.input_adaptor.database, self.input_adaptor.table, self.input_adaptor.primary_key, self.input_adaptor.parameter, self.input_adaptor.value)
#        elif cmd == "get":
#            return GetCommand(self.input_adaptor.database, self.input_adaptor.table, self.input_adaptor.primary_key)
#        elif cmd == "delete":
#            return DeleteCommand(self.input_adaptor.database, self.input_adaptor.table, self.input_adaptor.primary_key)

    def validate(self):
        if self.input_adaptor.command is None:
            raise NoParameterError()
        if not (self.input_adaptor.command == "set" or self.input_adaptor.command == "get" or self.input_adaptor.command == "delete" or self.input_adaptor.command == "create"):
            raise WrongParameterError()
