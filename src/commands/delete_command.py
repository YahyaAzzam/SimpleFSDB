from commands.abstract_command import *
from model.database import *


class DeleteCommand(AbstractCommand):
    def __init__(self, database_name, table_name, data):
        self.data = DeleteCommand.validate(database_name, data)
        self.database_name = database_name
        self.table_name = table_name

    def execute(self):
        database = Database(database_name = self.database_name)
        database.delete(self.table_name, self.data)

    @staticmethod
    def validate(database_name, data):
        if database_name == None or len(database_name) == 0:
            raise NoParameterError("database_name parameter not entered")
        try:
            if data == "None":
                raise NoParameterError("data parameter not entered")
            return eval(data)
        except:
            raise NoParameterError("data parameter not entered")
