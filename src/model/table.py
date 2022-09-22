import os

from model.table_metadata import *


class Table:
    def __init__(self, database, table_name, table=None):
        self.__path__ = os.path.join(database.get_path(), table_name)
        if table is None:
            table = TableMetaData.get_table_schema(self.__path__, table_name)
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
        efficient_index = self.__get_efficient_index__(query)
        if efficient_index is None:
            efficient_keys = self.__get_all_primary_keys__()
        else:
            efficient_keys = efficient_index.get_primary_keys(query[efficient_index.name])
        found_objects = self.__get_rows__(efficient_keys)
        return self.__filter_by_query__(found_objects, query)

    def __get_efficient_index__(self, query):
        if not query or str(query).isspace:
            return None
        if self.__table_metadata__.primary_key in query.keys():
            return Index(self.__table_metadata__.primary_key, self.__table_metadata__)
        index_names = set(self.__table_metadata__.get_indices_names())
        most_efficient = None
        for item in query.keys():
            if item in index_names:
                current_index = self.__table_metadata__.get_index(item)
                if most_efficient is None or current_index.compare(most_efficient) == -1:
                    most_efficient = current_index
        return most_efficient

    def __get_all_primary_keys__(self):
        primary_keys = []
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

    def __get_rows__(self, primary_keys):
        if primary_keys is None or len(primary_keys) == 0:
            raise WrongParameterError("No attributes found")
        rows = []
        for primary_key in primary_keys:
            rows.append(self.get_by_primary_key(str(primary_key).replace("json", '')))
        return rows
