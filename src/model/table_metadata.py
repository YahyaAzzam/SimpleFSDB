from model.index import *


class TableMetaData:
    def __init__(self, table, table_name = None):
        self.__path__ = table.get_path()
        if table.table_schema is not None:
            TableMetaData.__validate__(table.table_schema)
            table_schema = table.table_schema
        elif table_name is not None:
            table_schema = self.load_table_schema(table_name)
        else:
            raise NoParameterError("Table not found")
        self.name = table_schema[Keys.NAME]
        self.primary_key = table_schema[Keys.PRIMARY_KEY]
        self.columns = table_schema[Keys.COLUMNS]
        self.overwrite = table_schema[Keys.OVERWRITE]
        self.index_keys = {}
        for index_name in table_schema[Keys.INDEX_KEYS]:
            self.index_keys[index_name] = Index(index_name, self)

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
        for index_name in self.index_keys:
            self.index_keys[index_name].serialize()

    @staticmethod
    def get_indices_names(index_keys):
        indices_names = []
        for index_name in index_keys:
            indices_names.append(index_name)
        return indices_names

    def load_table_schema(self, table_name):
        with open(os.path.join(self.__path__, "{}_schema.json".format(table_name)), 'r') as file:
            return json.load(file)