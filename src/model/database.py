from model.table import *


class Database:
    DATABASE_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'storage')
    def __init__(self, schema_data = None, database_name = None):
        Database.__validate__(schema_data, database_name)
        if schema_data is not None:
            self.__initialize_by_schema_data__(schema_data)
        else:
            self.__initialize_by_database_name__(database_name)

    def __initialize_by_schema_data__(self, schema_data):
        self.__path__ = os.path.join(self.DATABASE_PATH, schema_data[Keys.DATABASE])
        self.__database_name__ = schema_data[Keys.DATABASE]
        self.tables = {}
        for table in schema_data[Keys.TABLES]:
            self.tables[table[Keys.NAME]] = Table(self, table)

    def __initialize_by_database_name__(self, database_name):
        self.__path__ = os.path.join(Database.DATABASE_PATH, database_name)
        if not os.path.exists(self.__path__):
            raise WrongParameterError("Wrong database entered")
        self.__database_name__ = database_name
        self.tables = {}
        for table in os.listdir(self.__path__):
            self.tables[str(table)] = Table(self, table_name=str(table))

    def get_path(self):
        return self.__path__

    def serialize(self):
        os.makedirs(self.__path__, exist_ok=True)
        self.__serialize_tables__()

    @staticmethod
    def __validate__(schema_data, database_name):
        if schema_data is None or len(schema_data[Keys.DATABASE]) == 0 or schema_data[Keys.DATABASE].isspace():
            if database_name is None or str(database_name).isspace():
                raise WrongParameterError("No database detected")

    def __serialize_tables__(self):
        for table in self.tables:
            self.tables[table].serialize()

    def get_table(self, table_name):
        if table_name not in self.tables:
            raise WrongParameterError("Wrong table entered")
        return self.tables[table_name]

    def set(self, table_name, values):
        table = self.get_table(table_name)
        return table.set(values)