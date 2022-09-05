from create_command import *

# from set_command import *
# from get_command import *
# from delete_command import *


class CommandFactory:
    def __init__(self, input_adaptor):
        self.input_adaptor = input_adaptor
        self.available_commands = {"create", "set", "get", "delete"}
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
        if self.input_adaptor.command == "none" or self.input_adaptor.command is None:
            raise NoParameterError("No command was entered")
        if self.input_adaptor.command not in self.available_commands:
            raise WrongParameterError("Wrong command entered")
