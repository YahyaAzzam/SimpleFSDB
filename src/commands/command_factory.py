from commands.create_command import *


# from set_command import *
# from get_command import *
# from delete_command import *


class CommandFactory:
    def __init__(self, input_adaptor):
        available_commands = {"create", "set", "get", "delete"}
        CommandFactory.validate(input_adaptor, available_commands)
        self.input_adaptor = input_adaptor

    def create(self):
        cmd = str(self.input_adaptor.command).lower()
        if cmd == "create":
            return CreateCommand(self.input_adaptor.schema_path)
    #        elif cmd == "set":
    #            return SetCommand(self.input_adaptor.database, self.input_adaptor.table, self.input_adaptor.primary_key, self.input_adaptor.parameter, self.input_adaptor.value)
        elif cmd == "get":
            return GetCommand(self.input_adaptor.database, self.input_adaptor.table, self.input_adaptor.values)
    #        elif cmd == "delete":
    #            return DeleteCommand(self.input_adaptor.database, self.input_adaptor.table, self.input_adaptor.primary_key)

    @staticmethod
    def validate(input_adaptor, available_commands):
        if input_adaptor.command not in available_commands:
            raise WrongParameterError("Wrong command entered")
