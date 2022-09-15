from commands.abstract_command import *
from model.database import *


class CreateCommand(AbstractCommand):
    def __init__(self, schema_path):
        CreateCommand.__validate__(schema_path)
        self.schema_data = self.__get_database_schema__(schema_path)

    def execute(self):
        database = Database(self.schema_data)
        database.serialize()

    @staticmethod
    def __validate__(schema_path):
        if len(schema_path) == 0 or schema_path.isspace():
            raise NoParameterError("schema_path parameter not entered")
        if not os.path.isfile(schema_path):
            raise WrongParameterError("Schema doesn't exist")

    @staticmethod
    def __get_database_schema__(schema_path):
        with open(schema_path, 'r') as file:
            return json.load(file)
