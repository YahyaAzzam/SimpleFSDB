import os
from output.exceptions import *


class Index:
    def __init__(self, index):
        self.index = index

    def validate(self, columns):
        if self.index is None or self.index not in columns:
            raise WrongParameterError("Index {} not found".format(self.index))

    def write(self, path):
        os.makedirs(os.path.join(path, self.index), exist_ok=True)
