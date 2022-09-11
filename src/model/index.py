import os
from output.exceptions import *
from commands.keys import Keys


class Index:
    def __init__(self, name, table_map):
        self.name = name
        self.table_map = table_map
        self.__validate__(self)

    @staticmethod
    def __validate__(self):
        if self.name not in self.table_map[Keys.COLUMNS]:
            raise WrongParameterError("Index {} not found".format(self.name))

    def serialize(self, path):
        os.makedirs(os.path.join(path, self.name), exist_ok=True)
