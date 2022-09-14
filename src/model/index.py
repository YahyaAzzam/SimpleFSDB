import os
import json
import pathlib
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

    @staticmethod
    def __validate_input__(value_name, path, value=0, primary_key=0):
        if value_name is None or value_name == "" or value_name == " ":
            raise NoParameterError("value_name parameter not entered")
        if not os.path.exists(os.path.join(path, "{}.json".format(value_name))):
            raise WrongParameterError("{} doesn't exist".format(value_name))
        if primary_key is None or primary_key == "" or primary_key == " ":
            raise NoParameterError("primary_key parameter not entered")
        if value is None or value == "" or value == " ":
            raise NoParameterError("value parameter not entered")

    def create(self):
        os.makedirs(self.path, exist_ok=True)

    def get_primary_keys(self, value_name):
        self.__validate_input__(value_name, self.path)
        with open(os.path.join(self.path, "{}.json".format(value_name)), 'r') as file:
            return json.load(file)

    def update_value(self, value_name, value):
        self.__validate_input__(value_name, self.path, value)
        with open(os.path.join(self.path, "{}.json".format(value_name)), 'w') as file:
            json.dump(value, file)

    def add_value(self, value_name, primary_key):
        self.__validate_input__(value_name, self.path, primary_key=primary_key)
        path = os.path.join(self.path, "{}.json".format(value_name))
        if os.path.exists(path):
            value = self.get_primary_keys(value_name)
            value["p_k"].append(primary_key)
            self.update_value(value_name, value)
        else:
            self.update_value(value_name, {"p_k": primary_key})

    def remove_value(self, value_name, primary_key):
        self.__validate_input__(value_name, self.path, primary_key=primary_key)
        value = self.get_primary_keys(value_name)
        if primary_key in value["p_k"]:
            value["p_k"].remove(primary_key)
        if not value["p_k"]:
            pathlib.Path(os.path.join(self.path, "{}.json".format(value_name))).unlink()
        else:
            self.update_value(value_name, value)
