from commands.abstract_command import *
from model.database import *


class CreateCommand(AbstractCommand):
    def __init__(self, schema_path):
        CreateCommand.__validate__(schema_path)
        self.schema_path = schema_path
        self.schema_data = self.__get_database_schema__()

    def execute(self):
        database = Database(self.schema_data)
        database.serialize()

    @staticmethod
    def __validate__(schema_path):
        schema_name = schema_path.replace(Keys.SCHEMA_PATH, '').replace("\\", '').replace("/", '')
        if len(schema_name) == 0 or schema_name.isspace():
            raise NoParameterError("schema_path parameter not entered")
        if not os.path.exists(schema_path):
            raise WrongParameterError("Schema doesn't exist")

    def __get_database_schema__(self):
        with open(self.schema_path, 'r') as file:
            return json.load(file)
