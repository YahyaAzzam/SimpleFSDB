import json
import os
from model.index import *
from commands.keys import Keys


class TableMetaData:
    def __init__(self, table_map):
        self.table_map = table_map
        self.name = table_map[Keys.NAME]
        self.columns = table_map[Keys.COLUMNS]
        self.primary_key = table_map[Keys.PRIMARY_KEY]
        self.index = table_map[Keys.INDEX_KEYS]
        self.validate(self)

    def serialize(self, path):
        path = os.path.join(path, self.name)
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, "{}_schema.json".format(self.name)), 'w') as file:
            json.dump(self.table_map, file)
        indices = Index(self.index, self.columns)
        indices.write(path)

    @staticmethod
    def validate(self):
        if self.primary_key is None or self.primary_key not in self.columns:
            raise WrongParameterError("Primary_key not found")
