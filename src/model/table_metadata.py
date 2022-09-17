from model.index import *


class TableMetaData:
    def __init__(self, table):
        TableMetaData.__validate__(table.table_schema)
        self.name = table.table_schema[Keys.NAME]
        self.primary_key = table.table_schema[Keys.PRIMARY_KEY]
        self.columns = table.table_schema[Keys.COLUMNS]
        self.__path__ = table.get_path()
        self.index_keys = []
        for index in table.table_schema[Keys.INDEX_KEYS]:
            self.index_keys.append(Index(index, self))

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
        indices = table_schema[Keys.INDEX_KEYS]
        table_schema.update({Keys.INDEX_KEYS: TableMetaData.__get_indices_names__(table_schema[Keys.INDEX_KEYS])})
        with open(os.path.join(path, "{}_schema.json".format(table_schema[Keys.NAME])), 'w') as file:
            json.dump(table_schema, file)
        table_schema.update({Keys.INDEX_KEYS: indices})

    def __serialize_indices__(self):
        for index in self.index_keys:
            index.serialize()

    @staticmethod
    def __get_indices_names__(index_keys):
        indices_names = []
        for index in index_keys:
            indices_names.append(index.name)
        return indices_names
