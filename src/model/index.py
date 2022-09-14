import os
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
