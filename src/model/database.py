from model.table import *


class Database:
    DATABASE_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'tests')
    
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
