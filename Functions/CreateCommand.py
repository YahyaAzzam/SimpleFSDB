from command_factory import *
from ICommand import ICommand
import json
import os
import keys

class CreateCommand(ICommand):
    def __init__(self, schema):
        self.schema = schema

    def execute(self):
        if self.schema is None:
            return "Schema not found"
        data = json.load(open(self.schema, 'r'))
        path = os.path.join(os.getcwd(), data[keys.DATABASE])
        os.makedirs(path, exist_ok=True)
        for table in data[keys.TABLES]:
            t_path = os.path.join(path, table[keys.NAME])
            os.makedirs(t_path, exist_ok=True)
        return "Database created successfully"
