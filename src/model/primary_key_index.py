from model.index import *


class PrimaryKeyIndex(Index):
    def __init__(self, primary_key_name, table_metadata):
        super().name = primary_key_name
        super().__path__ = table_metadata.get_path()

    def __get_primary_key_path__(self, primary_key):
        return os.path.join(super().__path__, "{}.json".format(primary_key))

    def __get_primary_key__(self, value):
        path = self.__get_primary_key_path__(value)
        if os.path.exists(path):
            return value
        return []
