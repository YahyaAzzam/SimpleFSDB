import os
import json
import pathlib
from output.exceptions import *
from commands.keys import *


class Index:
    def __init__(self, name, path, table):
        self.__validate__(name, table[Keys.COLUMNS])
        self.name = name
        self.path = os.path.join(path, self.name)

    @staticmethod
    def __validate__(name, table_columns):
        if name not in table_columns:
            raise WrongParameterError("Index {} not found".format(self.name))

    @staticmethod
    def __validate_input__(value_name, path, primary_keys="-1", primary_key="-1"):
        if len(value_name) == 0 or value_name.isspace():
            raise NoParameterError("value_name parameter not entered")
        if not os.path.exists(os.path.join(path, "{}.json".format(value_name))):
            raise WrongParameterError("{} doesn't exist".format(value_name))
        if len(primary_key) == 0 or primary_key.isspace():
            raise NoParameterError("primary_key parameter not entered")
        if len(primary_keys) == 0 or primary_keys.isspace():
            raise NoParameterError("value parameter not entered")

    def serialize(self):
        os.makedirs(self.path, exist_ok=True)

    def get_primary_keys(self, value_name):
        self.__validate_input__(value_name, self.path)
        with open(os.path.join(self.path, "{}.json".format(value_name)), 'r') as file:
            return json.load(file)

    @staticmethod
    def __update_value__(path, value_name, primary_keys):
        self.__validate_input__(value_name, path, primary_keys)
        with open(os.path.join(path, "{}.json".format(value_name)), 'w') as file:
            json.dump(primary_keys, file)

    def add_value(self, value_name, primary_key):
        self.__validate_input__(value_name, self.path, primary_key=primary_key)
        path = os.path.join(self.path, "{}.json".format(value_name))
        if os.path.exists(path):
            value = self.get_primary_keys(value_name)
            value["p_k"].append(primary_key)
            self.__update_value__(self.path, value_name, value)
        else:
            self.__update_value__(self.path, value_name, {"p_k": primary_key})

    def remove_value(self, value_name, primary_key):
        self.__validate_input__(value_name, self.path, primary_key=primary_key)
        value = self.get_primary_keys(value_name)
        if primary_key in value["p_k"]:
            value["p_k"].remove(primary_key)
        if not value["p_k"]:
            pathlib.Path(os.path.join(self.path, "{}.json".format(value_name))).unlink()
        else:
            self.__update_value__(self.path, value_name, value)
