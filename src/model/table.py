from model.table_metadata import *


class Table:
    def __init__(self, database_name, table_map, path):
        self.table_metadata = TableMetaData(database_name, table_map, path)

    def serialize(self):
        os.makedirs(self.table_metadata.path, exist_ok=True)
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
