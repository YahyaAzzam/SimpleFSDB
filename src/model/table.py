import os

from model.table_metadata import *


class Table:
    def __init__(self, database, table_name, table=None):
        if table is None:
            table = TableMetaData.get_table_schema(database.get_path(), table_name)
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

    def get(self, query):
        best_search = self.__get_efficient_primary_keys__(query)
        found_objects = self.get_rows(best_search)
        return self.__filter_by_query__(found_objects, query)

    def __get_efficient_primary_keys__(self, query):
        index_names = self.__table_metadata__.get_indices_names()
        primary_keys = []
        if query is not None or query != "" or not str(query).isspace:
            if self.__table_metadata__.primary_key in query.values:
                primary_keys.append(query[self.__table_metadata__.primary_key])
            else:
                for item in query.items():
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
        if not os.path.exists(path):
            return None
        with open(path, 'r') as file:
            return json.load(file)

    @staticmethod
    def __filter_by_query__(found_objects, query):
        if query and not str(query).isspace:
            for object_to_compare in found_objects:
                for value_to_compare in query.items:
                    if value_to_compare[1] != object_to_compare[value_to_compare[0]]:
                        found_objects.remove(object_to_compare)
                        break
        return found_objects

    def get_rows(self, primary_keys):
        if primary_keys is None or len(primary_keys) == 0:
            raise WrongParameterError("No attributes found")
        rows = []
        for primary_key in primary_keys:
            rows.append(self.get_by_primary_key(str(primary_key).replace("json", '')))
        return rows
