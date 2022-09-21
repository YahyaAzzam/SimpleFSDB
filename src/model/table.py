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
    def __set_file__(self, data):
        primary_key = data[self.__table_metadata__.primary_key]
        if os.path.exists(os.path.join(self.__path__, "{}.json".format(primary_key))):
            if eval(self.__table_metadata__.overwrite):
                unwanted_data = self.get_by_primary_key(primary_key)
                Table.delete_index(unwanted_data, self.__table_metadata__.index_keys, primary_key)
            else:
                raise WrongParameterError("can't set this file")
        Table.add_to_index(data, self.__table_metadata__.index_keys, primary_key)
        Table.__create_row__(data, primary_key, self.__path__)

    def set(self, data):
        primary_key = self.__table_metadata__.primary_key
        if primary_key not in data:
            self.__set_all__(data)
        else:
            self.__set_file__(data)

    @staticmethod
    def __create_row__(data, primary_key, path):
        with open(os.path.join(path, "{}.json".format(primary_key)), 'w') as file:
            json.dump(data,file)

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

    def __set_all__(self, data):
        if eval(self.__table_metadata__.overwrite):
            for file in os.listdir(self.__path__):
                if file == "{}_schema.json".format(self.__table_metadata__.name):
                    continue
                if file in TableMetaData.get_indices_names(self.__table_metadata__.index_keys):
                    continue
                unwanted_data = self.get_by_primary_key(file.replace(".json",""))
                Table.delete_index(unwanted_data, self.__table_metadata__.index_keys, file.replace(".json",""))
                Table.add_to_index(data, self.__table_metadata__.index_keys, file.replace(".json",""))
                Table.__create_row__(data, file.replace(".json",""), self.__path__)
        else:
            raise WrongParameterError("can't set this table")

    def delete(self):
        pass

    def get(self):
        pass

    def get_by_primary_key(self, primary_key):
        path = os.path.join(self.__path__, "{}.json".format(primary_key))
        with open(path, 'r') as file:
            return json.load(file)
