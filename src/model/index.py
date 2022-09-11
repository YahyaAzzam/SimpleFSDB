import os
from output.exceptions import *


class Index:
    def __init__(self, names, columns):
        self.names = names
        self.validate(self, columns)

    @staticmethod
    def validate(self, columns):
        for name in self.names:
            if name not in columns:
                raise WrongParameterError("Index {} not found".format(name))

    def write(self, path):
        for name in self.names:
            os.makedirs(os.path.join(path, name), exist_ok=True)
