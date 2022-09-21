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
        efficient_keys = self.__get_efficient_primary_keys__(efficient_index)
        found_objects = self.get_rows(efficient_keys)
        return self.__filter_by_query__(found_objects, query)

    def __get_efficient_index__(self, query):
        index_names = self.__table_metadata__.get_indices_names()
        index = {}
        keys_number = None
        if not query or str(query).isspace:
            return None
        if self.__table_metadata__.primary_key in query.keys():
            index = {self.__table_metadata__.primary_key: query[self.__table_metadata__.primary_key]}
        else:
            for item in query.keys():
                if item in index_names:
                    number_of_keys = len(self.__table_metadata__.get_index_primary_keys(item, query[item]))
                    if keys_number is None or number_of_keys < keys_number:
                        keys_number = number_of_keys
                        index.update({item: query[item]})
        return index

    def __get_efficient_primary_keys__(self, index):
        primary_keys = []
        if index is None:
            for primary_key in os.listdir(self.__path__):
                if ".json" in str(primary_key) and "schema" not in str(primary_key):
                    primary_keys.append(self.get_by_primary_key(str(primary_key).replace(".json", '')))
        elif self.__table_metadata__.primary_key in index.keys():
            primary_keys.append(index[self.__table_metadata__.primary_key])
        else:
            index = index.items()
            primary_keys = self.__table_metadata__.get_index_primary_keys(index[0], index[1])
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
