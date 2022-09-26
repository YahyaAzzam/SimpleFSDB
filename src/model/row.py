import uuid
import os
import json
import pathlib

class Row:
    def __init__(self, table, data):
        self.table = table
        self.data = data
        self.primary_key = self.__get_primary_key__(data.get(table.get_primary_key()))
        self.data[table.get_primary_key()] = self.primary_key
        self.__lock_path__ = os.path.join(self.table.get_data_path(), "Lock", "{}.json".format(self.primary_key))

    def __get_primary_key__(self, primary_key):
        primary_key = primary_key if primary_key else str(uuid.uuid4().hex)
        return primary_key

    def get_row_path(self, primary_key=None):
        primary_key = primary_key if primary_key else self.primary_key
        return os.path.join(self.table.get_data_path(), "{}.json".format(primary_key))

    def row_exists(self):
        return os.path.exists(self.get_row_path())

    def serialize(self):
        self.__lock__()
        with open(self.get_row_path(), 'w') as file:
           json.dump(self.data, file)
        self.__add_to_index__()
        pathlib.Path(self.__lock_path__).unlink()

    def __add_to_index__(self):
        indices = self.table.get_indices()
        for index in indices:
            if index != self.table.get_primary_key() and index in self.data:
                indices[index].add_value(self.data[index], self.primary_key)

    def __delete_index__(self):
        indices = self.table.get_indices()
        for index in indices:
            if index != self.table.get_primary_key() and index in self.data:
                indices[index].remove_value(self.data[index], self.primary_key)

    def delete(self):
        self.__check_lock__()
        self.__delete_index__()

    @staticmethod
    def load_by_primary_key(table, primary_key):
        path = os.path.join(table.get_data_path(), "{}.json".format(primary_key))
        if not (path and os.path.isfile(path)):
            return None
        with open(path, 'r') as file:
            data = json.load(file)
        return Row(table, data)

    def compare(self, query):
        for attribute in query.items():
            if not self.data or attribute[1] != self.data[attribute[0]]:
                return False
        return True

    def __lock__(self):
        self.__check_lock__()
        with open(self.__lock_path__, 'w') as file:
            pass

    def __check_lock__(self):
        while(os.path.exists(self.__lock_path__)):
            pass
