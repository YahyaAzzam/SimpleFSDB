from functions import *


class ICommand:
    def execute(self):
        pass


class command_factory:
    @staticmethod
    def create(args):
        cmd = args.command.lower()
        if cmd == "create_dir":
            make = create_dir_command(args.schema).execute()
            if make:
                print('Database already exists')
            return
        elif cmd == "create":
            make = create_command(args.schema, args.table, args.primary_key).execute()
            if not make:
                print('Database not found')
            elif make == 2:
                print('Destination already exists')
            return
        elif cmd == "set":
            set_command(args.database, args.table, args.primary_key, args.parameter, args.value).execute()
            return
        elif cmd == "get":
            make = get_command(args.database, args.table, args.primary_key).execute()
            if not make:
                return "Error, data not found"
            else:
                return make
        elif cmd == "delete":
            make = delete_command(args.database, args.table, args.primary_key).execute()
            if not make:
                return "Error, data not found"
