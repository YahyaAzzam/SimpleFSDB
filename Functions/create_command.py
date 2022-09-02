from SimpleFSDB.Command.abstract_command import *
import json
import os
from SimpleFSDB.Command.keys import Keys
from SimpleFSDB.Command.errors import *


class CreateCommand(AbstractCommand):
    def __init__(self, schema_file):
        self.data = None
        self.path = None
        self.schema_file = schema_file
        self.schema_dir = os.path.dirname(Keys.SCHEMA)
        self.database_dir = os.path.dirname(Keys.SCHEMA)
        self.validate()
        file = open(self.schema_file, 'r')
        self.data = json.load(file)
        file.close()
        self.check_database()

    def execute(self):
        self.path = os.path.join(self.database_dir, self.data[Keys.DATABASE])
        os.makedirs(self.path, exist_ok=True)
        for table in self.data[Keys.TABLES]:
            t_path = os.path.join(self.path, table[Keys.NAME])
            os.makedirs(t_path, exist_ok=True)
        return "database created successfully"

    def validate(self):
        if self.schema_file is None or self.schema_file == "" or self.schema_file == " ":
            raise NoParameterError()
        path = os.path.join(self.schema_dir, str(self.schema_file))
        if not os.path.exists(path):
            raise WrongParameterError()

    def check_database(self):
        if self.data[Keys.DATABASE] is None:
            raise NoDatabaseError()
