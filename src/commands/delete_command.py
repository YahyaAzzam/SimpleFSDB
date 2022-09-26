from commands.abstract_command import *
from model.database import *


class DeleteCommand(AbstractCommand):
    def __init__(self, database_name, table_name, query):
        self.query = DeleteCommand.validate(database_name, query)
        self.database_name = database_name
        self.table_name = table_name

    def execute(self):
        database = Database(database_name = self.database_name)
        database.delete(self.table_name, self.query)

    @staticmethod
    def validate(database_name, query):
        if database_name == None or len(database_name) == 0:
            raise NoParameterError("database_name parameter not entered")
        try:
            if query == "None":
                raise NoParameterError("data parameter not entered")
            return eval(query)
        except:
            raise NoParameterError("data parameter not entered")
