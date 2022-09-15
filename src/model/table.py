from model.table_metadata import *


class Table:
    def __init__(self, database, table):
        self.__path__ = os.path.join(database.get_path(), table[Keys.NAME])
        self.__table_metadata__ = TableMetaData(table, self)

    def serialize(self):
        os.makedirs(self.__path__, exist_ok=True)
        self.__table_metadata__.serialize()

    def get_path(self):
        return self.__path__

    # Will be implemented later in the project
    def set(self):
        pass

    def delete(self):
        pass

    def get(self):
        pass

    def get_by_primary_key(self):
        pass
