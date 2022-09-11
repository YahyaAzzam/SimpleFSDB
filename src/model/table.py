import json
import os
from model.index import *


class TableMetaData:
    def __init__(self, table_map):
        self.table_map = table_map
        self.__validate__(self)

    def serialize(self, path):
        path = os.path.join(path, self.table_map[Keys.NAME])
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, "{}_schema.json".format(self.table_map[Keys.NAME])), 'w') as file:
            json.dump(self.table_map, file)
        self.__create_indices__(path)

    def __create_indices__(self, path):
        for index in self.table_map[Keys.INDEX_KEYS]:
            index = Index(index, self.table_map)
            index.serialize(path)

    @staticmethod
    def __validate__(self):
        if self.table_map[Keys.PRIMARY_KEY] is None or self.table_map[Keys.PRIMARY_KEY] not in self.table_map[Keys.COLUMNS]:
            raise WrongParameterError("Primary_key not found")
