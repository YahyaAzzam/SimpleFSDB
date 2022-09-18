from model.table_metadata import *


class Table:
    def __init__(self, database, table):
        self.table_schema = table
        self.__path__ = os.path.join(database.get_path(), table[Keys.NAME])
        self.__table_metadata__ = TableMetaData(self)

    def serialize(self):
        os.makedirs(self.__path__, exist_ok=True)
        self.__table_metadata__.serialize()

    def get_name(self):
        return self.__table_metadata__.name

    def get_path(self):
        return self.__path__

    # Will be implemented later in the project
    def set(self, value, overwrite):
        primary_key = value[self.__table_metadata__.primary_key]
        if overwrite and os.path.exists(os.path.join(self.__path__, "{}.json".format(primary_key))):
            unwanted_value = self.get_by_primary_key(primary_key)
            Table.clean_index(unwanted_value, self.__table_metadata__.index_keys, primary_key)
        for index in self.__table_metadata__.index_keys:
            if index.name in value:
                index.add_value(value[index.name], primary_key)
        with open(os.path.join(self.__path__, "{}.json".format(primary_key)), 'w') as file:
            json.dump(value, file)

    @staticmethod
    def clean_index(value, indices, primary_key):
            for index in indices:
                if index.name in value:
                    index.remove_value(value[index.name], primary_key)

    def delete(self):
        pass

    def get(self):
        pass

    def get_by_primary_key(self, primary_key):
        path = os.path.join(self.__path__, "{}.json".format(primary_key))
        with open(path, 'r') as file:
            return json.load(file)
