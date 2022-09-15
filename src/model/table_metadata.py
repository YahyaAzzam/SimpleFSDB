from model.index import *


class TableMetaData:
    def __init__(self, database_schema, name, path):
        table_map = TableMetaData.__get_table_map__(database_schema, name)
        TableMetaData.__validate__(table_map)
        self.table_name = table_map[Keys.NAME]
        self.primary_key = table_map[Keys.PRIMARY_KEY]
        self.columns = table_map[Keys.COLUMNS]
        self.database_name = database_schema[Keys.DATABASE]
        self.path = os.path.join(path, self.table_name)
        self.indices = []
        for index in table_map[Keys.INDEX_KEYS]:
            self.indices.append(Index(index, self.path, table_map))

    def serialize(self):
        self.__create_table_schema__()
        self.__serialize_indices__()

    @staticmethod
    def __validate__(table_map):
        if table_map[Keys.PRIMARY_KEY] is None or table_map[Keys.PRIMARY_KEY] not in table_map[Keys.COLUMNS]:
            raise WrongParameterError("Primary_key not found")

    def __create_table_schema__(self):
        self.table_object = {Keys.DATABASE: self.database_name, Keys.NAME: self.table_name, Keys.PRIMARY_KEY: self.primary_key, Keys.COLUMNS: self.columns, Keys.INDEX_KEYS: self.indices}
        with open(os.path.join(self.path, "{}_schema.json".format(self.table_name)), 'w') as file:
            json.dump(self.table_object, file)

    def __serialize_indices__(self):
        for index in self.indices:
            index.serialize()

    @staticmethod
    def __get_table_map__(database_schema, name):
        for table_map in database_schema[Keys.TABLES]:
            if table_map[Keys.NAME] == name:
                return table_map
