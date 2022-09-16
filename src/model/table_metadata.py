from model.index import *


class TableMetaData:
    def __init__(self, table_schema, table):
        TableMetaData.__validate__(table_schema)
        self.name = table_schema[Keys.NAME]
        self.primary_key = table_schema[Keys.PRIMARY_KEY]
        self.columns = table_schema[Keys.COLUMNS]
        self.__path__ = table.get_path()
        self.indices = []
        for index in table_schema[Keys.INDEX_KEYS]:
            self.indices.append(Index(index, self))

    def get_path(self):
        return self.__path__

    def serialize(self):
        TableMetaData.__create_table_schema__(self.__dict__, self.__path__)
        self.__serialize_indices__()

    @staticmethod
    def __validate__(table_schema):
        if table_schema[Keys.PRIMARY_KEY] is None or table_schema[Keys.PRIMARY_KEY] not in table_schema[Keys.COLUMNS]:
            raise WrongParameterError("Primary_key not found")

    @staticmethod
    def __create_table_schema__(table_schema, path):
        with open(os.path.join(path, "{}_schema.json".format(table_schema[Keys.NAME])), 'w') as file:
            json.dump(table_schema, file)

    def __serialize_indices__(self):
        for index in self.indices:
            index.serialize()
