from model.table import *


class Database:

    def __init__(self, schema_name):
        self.__get_database_schema__(schema_name)
        self.name = self.database_object[Keys.DATABASE]
        self.__validate_name__()
        self.path = os.path.join(Keys.DATABASE_PATH, self.name)

    def serialize(self):
        self.__create_database__()
        self.__create_tables__()

    def __validate_name__(self):
        if self.name is None:
            raise WrongParameterError("No database detected")

    def __get_database_schema__(self, schema_name):
        schema_file = os.path.join(Keys.SCHEMA_PATH, schema_name)
        with open(schema_file, 'r') as file:
            self.database_object = json.load(file)

    def __create_database__(self):
        os.makedirs(self.path, exist_ok=True)

    def __create_tables__(self):
        for table in self.database_object[Keys.TABLES]:
            table_object = Table(self.database_object[Keys.DATABASE], table, self.path)
            table_object.serialize()
