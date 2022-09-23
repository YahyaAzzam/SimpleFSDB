from model.index import *


class PrimaryKeyIndex(Index):
    def __init__(self, primary_key_name, table_metadata):
        super().name = primary_key_name
        super().__path__ = table_metadata.get_path()

    def add_value(self):
        pass

    def remove_value(self):
        pass
