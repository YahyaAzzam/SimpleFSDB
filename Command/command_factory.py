import sys,os
sys.path.append(os.path.join(os.getcwd(), "Functions"))
from CreateCommand import *
from SetCommand import *
from GetCommand import *
from DeleteCommand import *



class CommandFactory:
    def __init__(self, args):
        self.command = args.command
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
        elif cmd == "set":
            return SetCommand(self.database, self.table, self.primary_key, self.parameter, self.value)
        elif cmd == "get":
            return GetCommand(self.database, self.table, self.primary_key)
        elif cmd == "delete":
            return DeleteCommand(self.database, self.table, self.primary_key)
