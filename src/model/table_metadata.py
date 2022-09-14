from model.index import *
from commands.keys import Keys


class TableMetaData:
    def __init__(self, database_name, table_map, path):
        self.__validate__(table_map)
        self.name = table_map[Keys.NAME]
        self.primary_key = table_map[Keys.PRIMARY_KEY]
        self.columns = table_map[Keys.COLUMNS]
        self.indices = table_map[Keys.INDEX_KEYS]
        self.database_name = database_name
        self.path = os.path.join(path, self.name)

    def serialize(self):
        self.__create_table_schema__()

    @staticmethod
    def __validate__(table_map):
        if table_map[Keys.PRIMARY_KEY] is None or table_map[Keys.PRIMARY_KEY] not in table_map[Keys.COLUMNS]:
            raise WrongParameterError("Primary_key not found")

    def __create_table_schema__(self):
        table_schema = {Keys.DATABASE: self.database_name, Keys.NAME: self.name, Keys.PRIMARY_KEY: self.primary_key,
                        Keys.COLUMNS: self.columns, Keys.INDEX_KEYS: self.indices}
        with open(os.path.join(self.path, "{}_schema.json".format(self.name)), 'w') as file:
            json.dump(table_schema, file)
