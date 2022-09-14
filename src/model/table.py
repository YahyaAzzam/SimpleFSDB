import os
from model.table_metadata import TableMetaData


class Table:

    def __init__(self, database_name, table_map, path):
        self.table_metadata = TableMetaData(table_map, path, database_name)

    def serialize(self):
        self.__create_table__()
        self.__create_indices__()

    # Will be implemented later in the project
    def write(self):
        pass

    def delete(self):
        pass

    def get(self):
        pass

    def get_by_primary_key(self):
        pass

    # Continue implemented (private) functions
    def __create_table__(self):
        os.makedirs(self.table_metadata.path, exist_ok=True)
        self.table_metadata.serialize()

    def __create_indices__(self):
        for index in self.table_metadata.indices:
            index = Index(index, self.table_metadata.columns, self.table_metadata.name, self.table_metadata.path)
            index.create()
