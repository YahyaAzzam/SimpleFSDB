import uuid
import os
import json
import pathlib


class Row:
    def __init__(self, table, data):
        self.__table__ = table
        self.__data__ = data
        self.__data__[table.get_primary_key()] = self.__get_primary_key__()
        self.__lock_path__ = os.path.join(self.__table__.get_lock_path(), "{}.json".format(self.get_primary_key()))

    def get_data(self):
        return self.__data__

    def __get_primary_key__(self):
        primary_key = self.__data__.get(self.__table__.get_primary_key()) if self.__data__.get(
            self.__table__.get_primary_key()) else str(uuid.uuid4().hex)
        return primary_key

    def get_primary_key(self):
        return self.__data__[self.__table__.get_primary_key()]

    def get_row_path(self):
        return os.path.join(self.__table__.get_data_path(), "{}.json".format(self.get_primary_key()))

    def row_exists(self):
        return os.path.exists(self.get_row_path())

    def serialize(self):
        self.__lock__()
        with open(self.get_row_path(), 'w') as file:
            json.dump(self.__data__, file)
        self.__add_to_index__()
        self.__unlock__()

    def __add_to_index__(self):
        indices = self.__table__.get_indices()
        for index in indices:
            if index != self.__table__.get_primary_key() and index in self.__data__:
                indices[index].add_value(self.__data__[index], self.get_primary_key())

    def __delete_index__(self):
        indices = self.__table__.get_indices()
        for index in indices:
            if index != self.__table__.get_primary_key() and index in self.__data__:
                indices[index].remove_value(self.__data__[index], self.get_primary_key())

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

    def has_attribute(self, query):
        for attribute in query.items():
            if not self.__data__ or attribute[1] != self.__data__[attribute[0]]:
                return False
        return True

    def __lock__(self):
        try:
            with open(self.__lock_path__, 'x'):
                pass
        except:
            self.__lock__()

    def __check_lock__(self):
        while os.path.exists(self.__lock_path__):
            pass

    def __unlock__(self):
        pathlib.Path(self.__lock_path__).unlink()
