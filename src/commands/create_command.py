from commands.abstract_command import *
from model.database import *


class CreateCommand(AbstractCommand):
    def __init__(self, schema_path):
        CreateCommand.__validate__(str(schema_path))
        self.schema_path = str(schema_path)
        self.schema_data = CreateCommand.__get_database_schema__(str(schema_path))

    def execute(self):
        database = Database(self.schema_data)
        database.serialize()
        database.update_databases_schemas(self.schema_path)

    @staticmethod
    def __validate__(schema_path):
        if  len(schema_path) == 0 or schema_path == "None":
            raise NoParameterError("schema_path parameter not entered")
        if not os.path.isfile(schema_path):
            raise WrongParameterError("Schema doesn't exist")

    @staticmethod
    def __get_database_schema__(schema_path):
        with open(schema_path, 'r') as file:
            return json.load(file)
