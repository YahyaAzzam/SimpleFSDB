from SimpleFSDB.Functions.create_command import *
from SimpleFSDB.Command.errors import *

# from set_command import *
# from get_command import *
# from delete_command import *


class CommandFactory:
    def __init__(self, args):
        self.command = args.command.lower()
        self.validate()
        self.schema = args.schema
        self.database = args.database
        self.table = args.table
        self.primary_key = args.primary_key
        self.parameter = args.parameter
        self.value = args.value

    def create(self):
        cmd = self.command
        if cmd == "create":
            return CreateCommand(self.schema)
#        elif cmd == "set":
#            return SetCommand(self.database, self.table, self.primary_key, self.parameter, self.value)
#        elif cmd == "get":
#            return GetCommand(self.database, self.table, self.primary_key)
#        elif cmd == "delete":
#            return DeleteCommand(self.database, self.table, self.primary_key)

    def validate(self):
        if self.command is None:
            raise NoParameterError()
        if not (self.command == "set" or self.command == "get" or self.command == "delete" or self.command == "create"):
            raise WrongParameterError()
