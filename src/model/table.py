import os

from model.table_metadata import *


class Table:
    def __init__(self, database, table):
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
    def set(self):
        pass

    def delete(self):
        pass

    def get(self, values):
        best_search = Table.__get_efficient__(values)
        found_objects = []
        if best_search == self.__table_metadata__.primary_key:
            found_objects.append(self.get_by_primary_key(values[best_search]))
        elif best_search in self.__table_metadata__.get_indices_names(self.__table_metadata__.index_keys):
            primary_keys = self.__table_metadata__.get_index_primary_keys(best_search, values[best_search])
            for primary_key in primary_keys:
                found_objects.append(self.get_by_primary_key(primary_key))
        else:
            found_objects.append(self.get_all_rows())
        return self.__compare_found__(found_objects, values)

    @staticmethod
    def __get_efficient__(values):
        item = values
        return item

    def get_by_primary_key(self, primary_key):
        path = os.path.join(self.__path__, "{}.json".format(primary_key))
        with open(path, 'r') as file:
            return json.load(file)

    @staticmethod
    def __compare_found__(found_objects, values):
        for object_to_compare in found_objects:
            finished_this = False
            for value_to_compare in values.items and finished_this:
                if value_to_compare[1] != object_to_compare[value_to_compare[0]]:
                    found_objects.remove(object_to_compare)
                    finished_this = True
        return found_objects

    def get_all_rows(self):
        rows = []
        for primary_key in os.listdir(self.__path__):
            if ".json" in str(primary_key) and "schema" not in str(primary_key):
                rows.append(self.get_by_primary_key(str(primary_key).replace(".json", '')))
        return rows
