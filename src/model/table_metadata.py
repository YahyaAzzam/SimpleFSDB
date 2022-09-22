from model.primary_key_index import *


class TableMetaData:
    def __init__(self, table):
        self.__path__ = table.get_path()
        self.name = table.table_schema[Keys.NAME]
        self.primary_key = table.table_schema[Keys.PRIMARY_KEY]
        self.columns = table.table_schema[Keys.COLUMNS]
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
        table_schema.update({Keys.INDEX_KEYS: TableMetaData.get_indices_names(table_schema[Keys.INDEX_KEYS])})
        with open(os.path.join(path, "{}_schema.json".format(table_schema[Keys.NAME])), 'w') as file:
            json.dump(table_schema, file)
        table_schema.update({Keys.INDEX_KEYS: indices})

    def __serialize_indices__(self):
        for index in self.index_keys:
            index.serialize()

    def get_indices_names(self):
        indices_names = []
        for index in self.index_keys:
            indices_names.append(index.name)
        return indices_names

    def get_index(self, index_name):
        for index in self.index_keys:
            if index.name == index_name:
                return index
        return None

    def get_index_primary_keys(self, index_name, index_value):
        for index in self.index_keys:
            if index.name == index_name:
                return index.get_primary_keys(index_value)
        raise WrongParameterError("Wrong index name entered")

    @staticmethod
    def get_table_schema(path, table_name):
        with open(os.path.join(path, "{}_schema.json".format(table_name)), 'r') as file:
            return json.loads(file)
