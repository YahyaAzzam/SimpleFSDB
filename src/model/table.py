from model.table_metadata import *


class Table:
    def __init__(self, database, table):
        self.path = os.path.join(database.path, table[Keys.NAME])
        self.table_metadata = TableMetaData(table, self)

    def serialize(self):
        os.makedirs(self.path, exist_ok=True)
        self.table_metadata.serialize()

    # Will be implemented later in the project
    def set(self):
        pass

    def delete(self):
        pass

    def get(self):
        pass

    def get_by_primary_key(self):
        pass
