from command_factory import *
from ICommand import ICommand
import json
import os
from keys import Keys

class CreateCommand(ICommand):
    def __init__(self, schema):
        self.schema = schema

    def execute(self):
        if self.schema is None or self.schema == "" or self.schema == " ":
            return "Schema not found"
        path = os.path.join(os.getcwd(), str(self.schema))
        if not os.path.exists(path):
            return "Schema not found"
        file = open(self.schema, 'r')
        data = json.load(file)
        file.close()
        path = os.path.join(os.getcwd(), data[Keys.DATABASE])
        os.makedirs(path, exist_ok = True)
        for table in data[Keys.TABLES]:
            t_path = os.path.join(path, table[Keys.NAME])
            os.makedirs(t_path, exist_ok = True)
        return "Database created successfully"
