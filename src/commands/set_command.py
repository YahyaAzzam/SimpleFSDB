from commands.abstract_command import *
from model.database import *


class SetCommand(AbstractCommand):
    def __init__(self, database_name, table_name, data = None):
        self.data = SetCommand.validate(database_name, table_name, data)
        self.database_name = database_name
        self.table_name = table_name

    def execute(self):
        database = Database(database_name = self.database_name)
        database.set(self.table_name, self.data)

    @staticmethod
    def validate(database_name, table_name, data):
        if database_name == None or len(database_name) == 0:
            raise NoParameterError("database_name parameter not entered")
        if table_name == None or len(table_name) == 0 or table_name.isspace():
            raise NoParameterError("table_name parameter not entered")
        try:
            if data == "None":
                return {}
            return eval(data)
        except:
            return {}