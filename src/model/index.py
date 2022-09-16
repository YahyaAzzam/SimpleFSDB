import os
import json
import pathlib
from output.exceptions import *
from model.schema_keys import *


class Index:
    def __init__(self, index_name, table_metadata):
        Index.__validate_index__(index_name, table_metadata.columns)
        self.name = index_name
        self.__path__ = os.path.join(table_metadata.get_path(), self.name)

    def get_path(self):
        return self.__path__

    @staticmethod
    def __validate_index__(index_name, table_columns):
        if index_name not in table_columns:
            raise WrongParameterError("Index {} not found".format(index_name))

    @staticmethod
    def __validate_value_name__(value_name):
        if len(value_name) == 0 or value_name.isspace():
            raise NoParameterError("value_name parameter not entered")

    def serialize(self):
        os.makedirs(self.__path__, exist_ok=True)

    def get_primary_keys(self, value_name):
        Index.__validate_value_name__(value_name)
        path = os.path.join(self.__path__, "{}.json".format(value_name))
        if os.path.exists(path):
            with open(path, 'r') as file:
                return json.load(file)
        else:
            return []

    @staticmethod
    def __update_value__(path, value_name, primary_keys):
        with open(os.path.join(path, "{}.json".format(value_name)), 'w') as file:
            json.dump(primary_keys, file)

    def add_value(self, value_name, primary_key):
            value = self.get_primary_keys(value_name)
            value.append(primary_key)
            self.__update_value__(self.path, value_name, value)

    def remove_value(self, value_name, primary_key):
        value = self.get_primary_keys(value_name)
        if primary_key in value:
            value.remove(primary_key)
        if not value:
            pathlib.Path(os.path.join(self.path, "{}.json".format(value_name))).unlink()
        else:
            self.__update_value__(self.path, value_name, value)
