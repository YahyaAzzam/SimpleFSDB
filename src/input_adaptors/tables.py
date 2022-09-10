import json
import os
from input_adaptors.index import *
from commands.keys import Keys


class Tables:
    def __init__(self, table_object):
        self.table_object = table_object
        self.name = table_object[Keys.NAME]
        self.columns = table_object[Keys.COLUMNS]
        self.primary_key = table_object[Keys.PRIMARY_KEY]
        self.index = table_object[Keys.INDEX_KEYS]

    def create_table(self, path):
        self.validate(self)
        path = os.path.join(path, self.name)
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, "{}_schema".format(self.name)), 'w') as file:
            json.dump(self.table_object, file)
        for index in self.index:
            index = Index(index)
            index.validate(self.index)
            index.write(path)

    @staticmethod
    def validate(self):
        if self.primary_key is None or self.primary_key not in self.columns:
            raise WrongParameterError("Primary_key not found")
