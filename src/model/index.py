import pathlib
import sys
import os
sys.path.append(os.path.dirname(__file__).replace("model", ''))
from output.exceptions import *
from model.schema_keys import *
from model.index_value import *


class Index:
    def __init__(self, index_name, table_metadata):
        Index.__validate_index__(index_name, table_metadata.columns)
        self.name = index_name
        self.__path__ = os.path.join(table_metadata.get_path(), "indices", self.name)

    def get_path(self):
        return self.__path__

    @staticmethod
    def __validate_index__(index_name, table_columns):
        if index_name not in table_columns:
            raise WrongParameterError("Index {} not found".format(index_name))

    def serialize(self):
        os.makedirs(self.__path__, exist_ok=True)

    def get_primary_keys(self, value_name):
        return IndexValue(self, value_name).get_primary_keys()

    def __update_value__(self, value_name, primary_keys):
        if not primary_keys:
            pathlib.Path(os.path.join(self.__path__, "{}.json".format(value_name))).unlink()
        else:
            with open(os.path.join(self.__path__, "{}.json".format(value_name)), 'w') as file:
                json.dump(primary_keys, file)

    def add_value(self, value_name, primary_key):
        primary_keys = self.get_primary_keys(value_name)
        primary_keys.append(primary_key)
        self.__update_value__(value_name, primary_keys)

    def remove_value(self, value_name, primary_key):
        primary_keys = self.get_primary_keys(value_name)
        if primary_key in primary_keys:
            primary_keys.remove(primary_key)
        self.__update_value__(value_name, primary_keys)

    def get_index_value(self, value_name):
        return IndexValue(self, value_name)
