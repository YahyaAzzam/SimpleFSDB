import json

from model.table import *


class Database:
    DATABASE_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'tests')
    SCHEMA_PATH = os.path.join(os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'tests'), "schemas.json")
    
    def __init__(self, schema_data):
        Database.__validate__(schema_data)
        self.__database_name__ = schema_data[Keys.DATABASE]
        self.__path__ = os.path.join(self.DATABASE_PATH, schema_data[Keys.DATABASE])
        self.tables = []
        for table in schema_data[Keys.TABLES]:
            self.tables.append(Table(self, table))

    def get_path(self):
        return self.__path__

    def serialize(self):
        os.makedirs(self.__path__, exist_ok=True)
        self.__serialize_tables__()

    @staticmethod
    def __validate__(schema_data):
        if len(schema_data[Keys.DATABASE]) == 0 or schema_data[Keys.DATABASE].isspace():
            raise WrongParameterError("No database detected")

    def __serialize_tables__(self):
        for table in self.tables:
            table.serialize()

    @staticmethod
    def get_schema(database_name):
        with open(Database.SCHEMA_PATH) as file:
            schema = json.load(file)
            if schema[database_name] is not None:
                return schema[database_name]
        raise WrongParameterError("Wrong database entered")

    def get_table(self, table_name):
        for table in self.tables:
            if table.get_name() == table_name:
                return table
        raise WrongParameterError("Wrong table entered")
