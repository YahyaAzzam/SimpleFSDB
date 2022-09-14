import json
import os
from commands.abstract_command import *
from model.table_metadata import *


class CreateCommand(AbstractCommand):
    def __init__(self, schema_file):
        self.validate(schema_file, Keys.SCHEMA_PATH)
        schema_file = os.path.join(Keys.SCHEMA_PATH, schema_file)
        with open(schema_file, 'r') as file:
            self.data = json.load(file)
        self.check_database()
        self.path = os.path.join(Keys.DATABASE_PATH, self.data[Keys.DATABASE])

    def execute(self):
        os.makedirs(self.path, exist_ok=True)
        for table in self.data[Keys.TABLES]:
            table_metadata = TableMetaData(table, self.path, self.data[Keys.NAME])
            table_metadata.serialize()

    @staticmethod
    def validate(schema_file, schema_dir):
        if schema_file is None or schema_file == "" or schema_file == " ":
            raise NoParameterError("Schema parameter not entered")
        path = os.path.join(schema_dir, str(schema_file))
        if not os.path.exists(path):
            raise WrongParameterError("Schema doesn't exist")

    def check_database(self):
        if self.data[Keys.DATABASE] is None:
            raise WrongParameterError("No database detected")
