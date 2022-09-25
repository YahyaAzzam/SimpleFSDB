import uuid
import os
import json
import pathlib
from model.file_mode import *


class Row:
    def __init__(self, table, data):
        self.table = table
        self.data = data
        self.primary_key = self.__get_primary_key__(data.get(table.get_primary_key()))
        self.data[table.get_primary_key()] = self.primary_key


    def __get_primary_key__(self, primary_key):
        primary_key = primary_key if primary_key else str(uuid.uuid4().node)
        return primary_key

    def get_path(self, primary_key=None):
        primary_key = primary_key if primary_key else self.primary_key
        return os.path.join(self.table.__get_data_path__(), "{}.json".format(primary_key))

    def serialize(self):
        with open(self.get_path(), FileMode(self.table.overwrite()).name) as file:
           json.dump(self.data, file)
        self.__add_to_index__()

    def __add_to_index__(self):
        indices = self.table.get_indices()
        for index in indices:
            if index != self.table.get_primary_key() and index in self.data:
                indices[index].add_value(self.data[index], self.primary_key)

    def delete_index(self):
        indices = self.table.get_indices()
        for index in indices:
            if index != self.table.get_primary_key() and index in self.data:
                indices[index].remove_value(self.data[index], self.primary_key)

    def delete(self):
        self.delete_index()
        pathlib.Path(self.get_path()).unlink()

    @staticmethod
    def load_by_primary_key(table, primary_key):
        path = os.path.join(table.__get_data_path__(), "{}.json".format(primary_key))
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
