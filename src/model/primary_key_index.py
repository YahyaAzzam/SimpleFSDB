from model.index import *


class PrimaryKeyIndex(Index):
    def __init__(self, primary_key_name, table_metadata):
        super().__init__(primary_key_name, table_metadata)

    def add_value(self):
        pass

    def remove_value(self):
        pass
