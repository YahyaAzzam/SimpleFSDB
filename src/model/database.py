from model.table import *


class Database:
    def __init__(self, schema_data):
        Database.__validate__(schema_data)
        self.schema_data = schema_data
        self.path = os.path.join(Keys.DATABASE_PATH, self.schema_data[Keys.DATABASE])
        self.tables = []
        for table in self.schema_data[Keys.TABLES]:
            self.tables.append(Table(self.schema_data, table[Keys.NAME], self.path))

    def serialize(self):
        self.__create_database__()
        self.__serialize_tables__()

    @staticmethod
    def __validate__(schema_data):
        if len(schema_data[Keys.DATABASE]) == 0 or schema_data[Keys.DATABASE].isspace():
            raise WrongParameterError("No database detected")

    def __create_database__(self):
        os.makedirs(self.path, exist_ok=True)

    def __serialize_tables__(self):
        for table in self.tables:
            table.serialize()
