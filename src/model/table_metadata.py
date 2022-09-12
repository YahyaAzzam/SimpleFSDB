import json
import os
from model.index import *


class TableMetaData:
    def __init__(self, table_map, path):
        self.name = table_map[Keys.NAME]
        self.primary_key = table_map[Keys.PRIMARY_KEY]
        self.columns = table_map[Keys.COLUMNS]
        self.indices = table_map[Keys.INDEX_KEYS]
        self.path = os.path.join(path, self.name)
        self.__validate__(self)
        self.serialize(table_map)

    def serialize(self, table_map):
        os.makedirs(self.path, exist_ok=True)
        with open(os.path.join(self.path, "{}_schema.json".format(self.name)), 'w') as file:
            json.dump(table_map, file)
        self.__create_indices__(self, table_map)

    @staticmethod
    def __create_indices__(self, table_map):
        for index in self.indices:
            index = Index(index, table_map, self.path)
            index.create()

    @staticmethod
    def __validate__(self):
        if self.primary_key is None or self.primary_key not in self.columns:
            raise WrongParameterError("Primary_key not found")
