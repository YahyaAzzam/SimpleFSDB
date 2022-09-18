import os

from model.table_metadata import *


class Table:
    def __init__(self, database, table):
        self.__path__ = os.path.join(database.get_path(), table[Keys.NAME])
        self.table_schema = table
        self.__table_metadata__ = TableMetaData(self)

    def serialize(self):
        os.makedirs(self.__path__, exist_ok=True)
        self.__table_metadata__.serialize()

    def get_name(self):
        return self.__table_metadata__.name

    def get_path(self):
        return self.__path__

    # Will be implemented later in the project
    def set(self):
        pass

    def delete(self):
        pass

    def get(self, values):
        best_search = Table.__get_efficient_primary_keys__(values)
        found_objects = self.get_rows(best_search)
        return self.__compare_found__(found_objects, values)

    def __get_efficient_primary_keys__(self, values):
        index_names = self.__table_metadata__.get_indices_names(self.__table_metadata__.index_keys)
        primary_keys = []
        for item in values.items():
            if item[0] == self.__table_metadata__.primary_key:
                primary_keys.append(item[1])
                break
            if item[0] in index_names:
                index_keys = self.__table_metadata__.get_index_primary_keys(str(item[0]), str(item[1]))
                primary_keys = index_keys if len(primary_keys) == 0 or len(primary_keys) > len(index_keys) else primary_keys
        if len(primary_keys) == 0:
            for primary_key in os.listdir(self.__path__):
                if ".json" in str(primary_key) and "schema" not in str(primary_key):
                    primary_keys.append(self.get_by_primary_key(str(primary_key).replace(".json", '')))
        return primary_keys

    def get_by_primary_key(self, primary_key):
        path = os.path.join(self.__path__, "{}.json".format(primary_key))
        with open(path, 'r') as file:
            return json.load(file)

    @staticmethod
    def __compare_found__(found_objects, values):
        for object_to_compare in found_objects:
            for value_to_compare in values.items:
                if value_to_compare[1] != object_to_compare[value_to_compare[0]]:
                    found_objects.remove(object_to_compare)
                    break
        return found_objects

    def get_rows(self, primary_keys):
        rows = []
        for primary_key in primary_keys:
            rows.append(self.get_by_primary_key(str(primary_key).replace("json", '')))
        return rows
