from model.table import *


class Database:
    DATABASE_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'storage')
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

    def get_table(self, table_name):
        for table in self.tables:
            if table.get_name() == table_name:
                return table
        raise WrongParameterError("Wrong table entered")

    def update_databases_schemas(self, schema_path):
        path = os.path.join(self.DATABASE_PATH, "databases_schemas.json")
        schemas = {}
        if os.path.exists(path):
            with open(path, 'r') as file:
                schemas = json.load(file)
        schemas[self.__database_name__] = schema_path
        with open(path, 'w') as file:
            json.dump(schemas, file)

    @staticmethod
    def get_schema_data(database_name):
        with open(os.path.join(Database.DATABASE_PATH, "databases_schemas.json")) as file:
            schema = json.load(file)
            if schema[database_name] is not None:
                with open(schema[database_name], 'r') as file:
                    return json.load(file)
            else:
                raise WrongParameterError("Wrong database entered")
