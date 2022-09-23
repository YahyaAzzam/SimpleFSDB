import os
import json


class IndexValue:
    def __init__(self, index, value_name):
        self.__index__ = index
        self.__value_name__ = value_name

    def get_primary_keys(self):
        if "PrimaryKeyIndex" in str(self.__index__.__class__):
            return [self.__value_name__]
        primary_keys = []
        path = os.path.join(self.__index__.get_path(), "{}.json".format(self.__value_name__))
        if os.path.isfile(path):
            with open(path, 'r') as file:
                primary_keys = json.load(file)
        return primary_keys

    def compare(self, value_to_compare):
        first_value = len(self.get_primary_keys())
        second_value = len(value_to_compare.get_primary_keys())
        return first_value - second_value

    def get_index(self):
        return self.__index__
