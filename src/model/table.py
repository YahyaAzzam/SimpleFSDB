from model.table_metadata import *
import time


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
        
    def get_primary_key(self):
        return self.__table_metadata__.primary_key

    # Will be implemented later in the project
    def __serialize_row__(self, data):
        primary_key = self.get_primary_key()
        can_overwrite = eval(self.__table_metadata__.overwrite)
        path = Table.__get_row_path__(self.__path__, data.get(primary_key))
        mode = 'w' if can_overwrite else 'x'
        data[self.get_primary_key()] = os.path.basename(path).replace(".json","")
        with open(path, mode) as file:
            json.dump(data, file)
        return data

    @staticmethod
    def generate_num(path):
        while os.path.exists(path):
            primary_key = int((time.time()*1000)%1e7)
            path = Table.__get_row_path__(path, primary_key)
        return primary_key

    @staticmethod
    def __get_row_path__(path, primary_key):
        if primary_key is None:
            primary_key = Table.generate_num(path)
        return os.path.join(path, "{}.json".format(primary_key))

    def set(self, data):
        primary_key = data.get(self.get_primary_key())
        existing_row = None
        if primary_key is not None:
            existing_row = self.get_by_primary_key(primary_key)
        try:
            self.delete(existing_row)
            data = self.__serialize_row__(data)
            Table.add_to_index(data, self.__table_metadata__.index_keys, data[self.get_primary_key()])
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
        if data is not None:
            primary_key = data[self.get_primary_key()]
            Table.delete_index(data, self.__table_metadata__.index_keys, primary_key)
        pass

    def get(self):
        pass

    def get_by_primary_key(self, primary_key):
        path = os.path.join(self.__path__, "{}.json".format(primary_key))
        if os.path.exists(path):
            with open(path, 'r') as file:
                return json.load(file)
