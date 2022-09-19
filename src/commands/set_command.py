from commands.abstract_command import *
from model.database import *


class SetCommand(AbstractCommand):
    def __init__(self, database, table, values):
        SetCommand.validate(str(database), str(table), values)
        self.database_name = str(database)
        self.table_name = str(table)
        self.values = eval(str(values))

    def execute(self):
        database = Database(database_name = self.database_name)
        database.set(self.table_name, self.values)

    @staticmethod
    def validate(database, table, values):
        if len(database) == 0 or database == "None":
            raise NoParameterError("database parameter not entered")
        if len(table) == 0 or table == "None":
            raise NoParameterError("table parameter not entered")
        if values == None :
            raise NoParameterError("values parameter not entered")
        if not isinstance(values, dict):
            raise WrongParameterError("values should be json")
