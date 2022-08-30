from functions import *


class CommandFactory:
    def create(args):
        cmd = args.command
        if cmd == "create_dir":
            check = CreateDirCommand(args.schema).execute()
            print(check)
            return
        elif cmd == "create":
            check = CreateCommand(args.schema, args.table, args.primary_key).execute()
            print(check)
            return
        elif cmd == "set":
            check = SetCommand(args.database, args.table, args.primary_key, args.parameter, args.value).execute()
            print(check)
            return
        elif cmd == "get":
            check = GetCommand(args.database, args.table, args.primary_key).execute()
            print(check)
        elif cmd == "delete":
            check = DeleteCommand(args.database, args.table, args.primary_key).execute()
            print(check)
