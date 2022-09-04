import sys
import json
import os
from abstract_command import *
from keys import Keys
sys.path.append(os.path.join(str(os.getcwd()).replace("commands", '').replace("tests", "src"), "output"))
from exceptions import *


class CreateCommand(AbstractCommand):
    def __init__(self, schema_file):
        self.schema_file = schema_file
        self.schema_dir = Keys.SCHEMA_PATH
        self.database_dir = Keys.SCHEMA_PATH
        self.validate()
        with open(self.schema_file, 'r') as file:
            self.data = json.load(file)
        self.check_database()
        self.path = os.path.join(self.database_dir, self.data[Keys.DATABASE])

    def execute(self):
        os.makedirs(self.path, exist_ok=True)
        for table in self.data[Keys.TABLES]:
            t_path = os.path.join(self.path, table[Keys.NAME])
            os.makedirs(t_path, exist_ok=True)

    def validate(self):
        if self.schema_file is None or self.schema_file == "" or self.schema_file == " ":
            raise NoParameterError("Schema parameter not entered")
        path = os.path.join(self.schema_dir, str(self.schema_file))
        if not os.path.exists(path):
            raise WrongParameterError("Schema doesn't exist")

    def check_database(self):
        if self.data[Keys.DATABASE] is None:
            raise WrongParameterError("No database detected")
