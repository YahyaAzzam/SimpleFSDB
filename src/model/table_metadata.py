import json
import os
from model.index import *


class TableMetaData:
    def __init__(self, table_map, path):
        self.table_map = table_map
        self.path = os.path.join(path, self.table_map[Keys.NAME])
        self.__validate__(self)
        self.serialize()

    def serialize(self):
        os.makedirs(self.path, exist_ok=True)
        with open(os.path.join(self.path, "{}_schema.json".format(self.table_map[Keys.NAME])), 'w') as file:
            json.dump(self.table_map, file)
        self.__create_indices__(self)

    @staticmethod
    def __create_indices__(self):
        for index in self.table_map[Keys.INDEX_KEYS]:
            index = Index(index, self.table_map, self.path)
            index.create()

    @staticmethod
    def __validate__(self):
        if self.table_map[Keys.PRIMARY_KEY] is None or self.table_map[Keys.PRIMARY_KEY] not in self.table_map[Keys.COLUMNS]:
            raise WrongParameterError("Primary_key not found")
