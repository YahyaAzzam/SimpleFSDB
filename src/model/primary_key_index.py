from model.index import *


class PrimaryKeyIndex(Index):
    def __init__(self, primary_key_name, table_metadata):
        super().name = primary_key_name
        super().value_name = None
        super().__path__ = table_metadata.get_path()

    def __get_primary_key_path__(self, primary_key):
        return os.path.join(super().__path__, "{}.json".format(primary_key))

    def __get_primary_keys__(self, value_name):
        super().value_name = value_name if value_name else super().value_name
        path = self.__get_primary_key_path__(super().value_name)
        if os.path.exists(path):
            return [super().value_name]
        return []

    @staticmethod
    def compare(index, value_name=None):
        super().value_name = value_name if value_name else super().value_name
        if len(index.get_primary_keys(index.value_name)):
            return -1
        return 1

    def add_value(self):
        pass

    def remove_value(self):
        pass
