import os, pathlib
from output.exceptions import *


class Index:
    def __init__(self, name, table_columns, table_name, path):
        self.__validate__(name, table_columns)
        self.table_name = table_name
        self.name = name
        self.table_columns = table_columns
        self.path = os.path.join(path, self.name)

    @staticmethod
    def __validate__(name, table_columns):
        if name not in table_columns:
            raise WrongParameterError("Index {} not found".format(self.name))

    def create(self):
        os.makedirs(self.path, exist_ok=True)

    def get_primary_keys(self, value_name):
        with open(os.path.join(self.path, "{}.json".format(value_name)), 'r') as file:
          return json.load(file)

    def update_value(self, value_name, value):
       with open(os.path.join(self.path, "{}.json".format(value_name)), 'w') as file:
           json.dump(value)

    def add_value(self, value_name, primary_key):
        path = os.path.join(self.path, value_name)
        if os.path.exists(path):
            value = self.get_primary_keys(value_name)
            value.append(primary_key)
            update_value(value_name, value)
        else:
            update_value(value_name, {primary_key})

    def remove_value(self, value_name, primary_key):
        path = os.path.join(self.path, value_name)
        if os.path.exists(path):
            value = self.get_primary_keys(value_name)
            value.discard(primary_key)
            if(value == {}):
                pathlib.Path(path).unlink()
            else:
                update_value(value_name, value)
