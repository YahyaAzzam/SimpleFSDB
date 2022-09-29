import sys
import os
sys.path.append(os.path.dirname(__file__).replace("commands", ''))
from commands.abstract_command import *
from output.exceptions import *
from model.database import *


class GetCommand(AbstractCommand):
    def __init__(self, database_name, table_name, query):
        GetCommand.validate(database_name, table_name)
        self.database_name = database_name
        self.table_name = table_name
        self.query = {} if not query else eval(query)

    def execute(self):
        database = Database(database_name=self.database_name)
        return database.get(self.table_name, self.query)

    @staticmethod
    def validate(database_name, table_name):
        if database_name is None or database_name == "" or database_name == " ":
            raise NoParameterError("Database parameter not entered")
        if table_name is None or table_name == "" or table_name == " ":
            raise NoParameterError("Table parameter not entered")
