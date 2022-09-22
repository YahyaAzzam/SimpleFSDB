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
    def __serialize_row__(self, data):
        primary_key = self.__table_metadata__.primary_key
        can_overwrite = eval(self.__table_metadata__.overwrite)
        path = self.get_row_path(data[primary_key])
        mode = 'w' if can_overwrite else 'x'
        with open(path, mode) as file:
            json.dump(data, file)
        return os.path.basename(path).replace(".json","")

    @staticmethod
    def generate_num():
        pass

    def get_row_path(self, primary_key):
        if primary_key is None:
            primary_key = Table.generate_num()
        return os.path.join(self.__path__, "{}.json".format(primary_key))

    def set(self, data):
        primary_key = data[self.__table_metadata__.primary_key]
        existing_row = None
        if primary_key is not None:
            existing_row = self.get_by_primary_key(primary_key)
        try:
            self.delete(existing_row)
            primary_key = self.__serialize_row__(data)
            Table.add_to_index(data, self.__table_metadata__.index_keys, primary_key)
        except:
            raise WrongParameterError("data exists")

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

    def delete(self, data):
        if data is None:
            return
        primary_key = data[self.__table_metadata__.primary_key]
        Table.delete_index(data, self.__table_metadata__.index_keys, primary_key)
        pass

    def get(self):
        pass

    def get_by_primary_key(self, primary_key):
        path = os.path.join(self.__path__, "{}.json".format(primary_key))
        if os.path.exists(path):
            with open(path, 'r') as file:
                return json.load(file)
