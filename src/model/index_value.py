import os
import json


class IndexValue:
    def __init__(self, index, value_name):
        self.index = index
        self.value_name = value_name

    def get_primary_keys(self, is_primary_key=False):
        if is_primary_key:
            return [self.value_name]
        primary_keys = []
        path = os.path.join(self.index.get_path(), "{}.json".format(self.value_name))
        if os.path.isfile(path):
            with open(path, 'r') as file:
                primary_keys = json.load(file)
        return primary_keys

    def compare(self, value_to_compare):
        first_value = len(self.get_primary_keys())
        second_value = len(value_to_compare.get_primary_keys())
        if first_value > second_value:
            return 1
        elif first_value < second_value:
            return -1
        return 0
