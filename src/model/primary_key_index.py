from model.index import *


class PrimaryKeyIndex(Index):
    def __init__(self, primary_key_name, table_metadata):
        super().name = primary_key_name
        super().__path__ = table_metadata.get_path()

    def __get_primary_key_path__(self, primary_key):
        return os.path.join(super().__path__, "{}.json".format(primary_key))

    def get_primary_keys(self, value_name):
        return IndexValue(self, value_name).get_primary_keys(is_primary_key=True)

    def add_value(self):
        pass

    def remove_value(self):
        pass
