import sys
import os
sys.path.append(os.path.dirname(__file__).replace("commands", ''))
from commands.create_command import *
from commands.set_command import *
from commands.get_command import *
from commands.delete_command import *
from commands.clear_command import *


class CommandFactory:
    def __init__(self, input_adaptor):
        available_commands = {"create", "set", "get", "delete", "clear"}
        CommandFactory.validate(input_adaptor, available_commands)
        self.input_adaptor = input_adaptor

    def create(self):
        cmd = str(self.input_adaptor.command).lower()
        if cmd == "create":
            return CreateCommand(self.input_adaptor.schema_path)
        elif cmd == "set":
            return SetCommand(self.input_adaptor.database, self.input_adaptor.table, self.input_adaptor.query)
        elif cmd == "get":
            return GetCommand(self.input_adaptor.database, self.input_adaptor.table, self.input_adaptor.query)
        elif cmd == "delete":
            return DeleteCommand(self.input_adaptor.database, self.input_adaptor.table, self.input_adaptor.query)
        elif cmd == "clear":
            return ClearCommand(self.input_adaptor.database)

    @staticmethod
    def validate(input_adaptor, available_commands):
        if input_adaptor.command not in available_commands:
            raise WrongParameterError("Wrong command entered")
