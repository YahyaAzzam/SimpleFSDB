import os
from commands.abstract_command import *
from model.database import *


class CreateCommand(AbstractCommand):
    def __init__(self, schema_name):
        self.validate(schema_name, Keys.SCHEMA_PATH)
        self.schema_name = schema_name

    def execute(self):
        self.__create_database__()

    @staticmethod
    def validate(schema_name, schema_dir):
        if schema_name is None or schema_name == "" or schema_name == " ":
            raise NoParameterError("Schema parameter not entered")
        path = os.path.join(schema_dir, str(schema_name))
        if not os.path.exists(path):
            raise WrongParameterError("Schema doesn't exist")

    def __create_database__(self):
        database = Database(self.schema_name)
        database.serialize()
