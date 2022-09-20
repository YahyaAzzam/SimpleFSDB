import json
from commands.abstract_command import *
from output.exceptions import *
from model.database import *


class GetCommand(AbstractCommand):

    def __init__(self, database, table, query):
        GetCommand.validate(database, table)
        self.database = database
        self.table = table
        if not query or str(query.isspace()):
            query = {}
        self.query = json.loads(query)

    def execute(self):
        database = Database(database_name=self.database)
        return database.get(self.table, self.query)

    @staticmethod
    def validate(database, table):
        if database is None or database == "" or database == " ":
            raise NoParameterError("Database parameter not entered")
        if table is None or table == "" or table == " ":
            raise NoParameterError("Table parameter not entered")
