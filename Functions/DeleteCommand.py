from command_factory import *
from ICommand import ICommand
import json
import os
import keys




class DeleteCommand(ICommand):

    def __init__(self, database, table, primary_key):
        self.database = database
        self.table = table
        self.primary_key = primary_key

    def execute(self):
        if self.database is None:
            return "Database not found"
        if self.table is None:
            return "Table not found"
        if self.primary_key is None:
            return "Primary key not found"
        path = os.path.join(os.getcwd(), self.database, self.table,self.primary_key)
        if os.path.exists(path):
            os.remove(path)
            return "Data deleted successfully"
        else:
            return "Data not found"
