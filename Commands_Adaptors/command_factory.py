from Functions.create_command import *

# from set_command import *
# from get_command import *
# from delete_command import *


class CommandFactory:
    def __init__(self, args):
        self.command = args[0]
        self.validate()
        self.schema = args[1]
        self.database = args[2]
        self.table = args[3]
        self.primary_key = args[4]
        self.parameter = args[5]
        self.value = args[6]

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
            return 1
        if not (self.command == "set" or self.command == "get" or self.command == "delete" or self.command == "create"):
            return 2
