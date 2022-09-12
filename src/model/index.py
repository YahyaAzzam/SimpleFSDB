import os
from output.exceptions import *
from commands.keys import Keys


class Index:
    def __init__(self, name, table_metadata, path):
        self.name = name
        self.table_metadata = table_metadata
        self.path = os.path.join(path, self.name)
        self.__validate__(self)

    @staticmethod
    def __validate__(self):
        if self.name not in self.table_metadata[Keys.COLUMNS]:
            raise WrongParameterError("Index {} not found".format(self.name))

    def create(self):
        os.makedirs(self.path, exist_ok=True)
