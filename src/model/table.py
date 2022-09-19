from model.table_metadata import *


class Table:
    def __init__(self, database, table_schema = None, table_name = None):
        if table_schema is None and table_name is None:
            raise NoParameterError("No table detected")
        self.__initialize_Table__(database, table_schema, table_name)

    def __initialize_Table__(self, database, table_schema, table_name):
        if table_schema is not None:
            self.__path__ = os.path.join(database.get_path(), table_schema[Keys.NAME])
            self.table_schema = table_schema
            self.__table_metadata__ = TableMetaData(self)
        else:
            self.__path__ = os.path.join(database.get_path(), table_name)
            self.table_schema = None
            self.__table_metadata__ = TableMetaData(self, table_name = table_name)
            self.table_schema = self.__table_metadata__.load_table_schema(table_name)

    def serialize(self):
        os.makedirs(self.__path__, exist_ok=True)
        self.__table_metadata__.serialize()

    def get_name(self):
        return self.__table_metadata__.name

    def get_path(self):
        return self.__path__

    # Will be implemented later in the project
    def set(self, values):
        Table.validate_set_values(self.__table_metadata__, values)
        primary_key = values[self.__table_metadata__.primary_key]
        if os.path.exists(os.path.join(self.__path__, "{}.json".format(primary_key))):
            unwanted_values = self.get_by_primary_key(primary_key)
            Table.clean_index(unwanted_values, self.__table_metadata__.index_keys, primary_key)
        Table.add_to_index(values, self.__table_metadata__.index_keys, primary_key)
        with open(os.path.join(self.__path__, "{}.json".format(primary_key)), 'w') as file:
            json.dump(values, file)

    @staticmethod
    def clean_index(values, indices, primary_key):
            for index in indices:
                if index in values:
                    indices[index].remove_value(values[index], primary_key)

    @staticmethod
    def add_to_index(values, indices, primary_key):
            for index in indices:
                if index in values:
                    indices[index].add_value(values[index], primary_key)

    @staticmethod
    def validate_set_values(table, values):
        primary_key = table.primary_key
        if primary_key not in values:
             raise WrongParameterError("primary_key is missing")
        table_columns = table.columns
        for input in values:
            if input not in table_columns:
                raise WrongParameterError("Wrong values")
        path = os.path.join(table.get_path(), "{}.json".format(values[primary_key]))
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

