from functions import *


class command_factory:
    def __init__(self, args):
        self.cmd = args.command.lower()
        self.args = args.lower()

    def execute(self):
        if self.cmd == "create_dir":
            m = creates_dir(self.args.schema)
            if m:
                print('Database already exists')
            return
        elif self.cmd == "create":
            m = creates(self.args.schema, self.args.table, self.args.primary_key)
            if not m:
                print('Database not found')
            elif m == 2:
                print('Destination already exists')
            return
        elif self.cmd == "set":
            sets(self.args.database, self.args.table, self.args.primary_key, self.args.parameter, self.args.value)
            return
        elif self.cmd == "get":
            m = gets(self.args.database, self.args.table, self.args.primary_key)
            if not m:
                return "Error, data not found"
            else:
                return m
        elif self.cmd == "delete":
            m = deletes(self.args.database, self.args.table, self.args.primary_key)
            if not m:
                return "Error, data not found"
