from model.table_metadata import *


class Table:
    def __init__(self, database,  table_name, table_schema = None):
        self.__path__ = os.path.join(database.get_path(), table_name)
        if table_schema is None:
            table_schema = TableMetaData.load_table_schema(self.__path__, table_name)
        self.table_schema = table_schema
        self.__table_metadata__ = TableMetaData(self)

    def serialize(self):
        os.makedirs(self.__path__, exist_ok=True)
        self.__table_metadata__.serialize()

    def get_name(self):
        return self.__table_metadata__.name

    def get_path(self):
        return self.__path__

    # Will be implemented later in the project
    def set(self, data):
        Table.validate_set_data(self.__table_metadata__, data)
        primary_key = data[self.__table_metadata__.primary_key]
        if os.path.exists(os.path.join(self.__path__, "{}.json".format(primary_key))):
            unwanted_data = self.get_by_primary_key(primary_key)
            Table.delete_index(unwanted_data, self.__table_metadata__.index_keys, primary_key)
        Table.add_to_index(data, self.__table_metadata__.index_keys, primary_key)
        Table.__create_row__(data, primary_key, self.__path__)

    @staticmethod
    def __create_row__(data, primary_key, path):
        with open(os.path.join(path, "{}.json".format(primary_key)), 'w') as file:
            json.dump(data, file)

    @staticmethod
    def delete_index(data, indices, primary_key):
            for index in indices:
                if index in data:
                    indices[index].remove_value(data[index], primary_key)

    @staticmethod
    def add_to_index(data, indices, primary_key):
            for index in indices:
                if index in data:
                    indices[index].add_value(data[index], primary_key)

    @staticmethod
    def validate_set_data(table, data):
        primary_key = table.primary_key
        if primary_key not in data:
             raise WrongParameterError("primary_key is missing")
        table_columns = table.columns
        for input in data:
            if input not in table_columns:
                raise WrongParameterError("Wrong data")
        path = os.path.join(table.get_path(), "{}.json".format(data[primary_key]))
        if os.path.exists(path) and not eval(table.overwrite):
                raise WrongParameterError("can't set this file")

    def delete(self):
        pass

    def get(self):
        pass

    def get_by_primary_key(self, primary_key):
        path = os.path.join(self.__path__, "{}.json".format(primary_key))
        with open(path, 'r') as file:
            return json.load(file)

