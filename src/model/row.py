import uuid
import os
import json
import pathlib
from model.file_mode import *


class Row:
    def __init__(self, table, data):
        self.table = table
        self.primary_key = self.__get_primary_key__(data.get(table.get_primary_key()))
        data[table.get_primary_key()] = self.primary_key
        self.data = data

    def __get_primary_key__(self, primary_key):
        if primary_key is not None:
            return primary_key
        path = self.table.get_path()
        while primary_key is None and os.path.exists(path):
            primary_key = uuid.uuid1().node
            path = self.get_path(primary_key)
        return primary_key

    def get_path(self, primary_key=None):
        primary_key = primary_key if primary_key else self.primary_key
        return os.path.join(self.table.__get_data_path__(), "{}.json".format(primary_key))

    @staticmethod
    def create(path, data, can_overwrite):
        with open(path, FileMode(can_overwrite).name) as file:
            json.dump(data, file)

    def serialize(self):
        can_overwrite = eval(self.table.overwrite())
        path = self.get_path()
        data = self.data
        Row.create(path, data, can_overwrite)
        self.__add_to_index__()

    def __add_to_index__(self):
        indices = self.table.get_indices()
        for index in indices:
            if index in self.data:
                indices[index].add_value(self.data[index], self.primary_key)

    def delete_index(self):
        indices = self.table.get_indices()
        for index in indices:
            if index in self.data:
                indices[index].remove_value(self.data[index], self.primary_key)

    def delete(self):
        self.delete_index()
        pathlib.Path(self.get_path()).unlink()
