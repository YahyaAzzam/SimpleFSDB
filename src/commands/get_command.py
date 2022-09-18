import json
from commands.abstract_command import *
from output.exceptions import *
from model.database import *


class GetCommand(AbstractCommand):

    def __init__(self, database, table, values):
        GetCommand.validate(database, table, values)
        self.database = database
        self.table = table
        self.values = json.loads(values)

    def execute(self):
        database = Database.get_database_by_name(self.database)
        table = database.get_table(self.table)
        return table.get(self.values)

    @staticmethod
    def validate(database, table, values):
        if database is None or database == "" or database == " ":
            raise NoParameterError("Database parameter not entered")
        if table is None or table == "" or table == " ":
            raise NoParameterError("Table parameter not entered")
        if values is None or values == "" or values == " ":
            raise NoParameterError("Values parameter not entered")
