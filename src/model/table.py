from model.table_metadata import *


class Table:
    def __init__(self, database, table_name, table=None):
        self.__path__ = os.path.join(database.get_path(), table_name)
        if table is None:
            table = TableMetaData.get_table_schema(self.__path__, table_name)
        self.table_schema = table
        self.__table_metadata__ = TableMetaData(self)

    def serialize(self):
        os.makedirs(self.__path__, exist_ok=True)
        os.makedirs(os.path.join(self.__path__, "data"), exist_ok=True)
        self.__table_metadata__.serialize()

    def get_name(self):
        return self.__table_metadata__.name

    def get_path(self):
        return self.__path__

    # Will be implemented later in the project
    def set(self):
        pass

    def delete(self):
        pass

    def get(self, query):
        efficient_index = self.__get_efficient_index__(query)
        if efficient_index is None:
            efficient_keys = self.__get_all_primary_keys__()
        else:
            efficient_keys = efficient_index.get_primary_keys()
        found_objects = self.__get_rows__(efficient_keys)
        return self.__filter_by_query__(found_objects, query)

    def __get_efficient_index__(self, query):
        if not query or str(query).isspace:
            return None
        most_efficient = None
        for item in query.keys():
            current_index = self.__table_metadata__.get_index(item)
            if current_index and (not most_efficient or current_index.compare(most_efficient, query[item]) == -1):
                most_efficient = current_index
        return most_efficient

    def __get_all_primary_keys__(self):
        primary_keys = []
        for primary_key_path in os.listdir(self.__get_data_path__()):
            primary_key = self.__get_primary_key_from_path__(primary_key_path)
            primary_keys.append(primary_key)
        return primary_keys

    def get_by_primary_key(self, primary_key):
        path = self.__get_primary_key_path__(primary_key)
        if not os.path.exists(path):
            return None
        with open(path, 'r') as file:
            return json.load(file)

    @staticmethod
    def __filter_by_query__(found_objects, query):
        if not query or str(query).isspace():
            return found_objects
        filtered_objects = []
        for object_to_compare in found_objects:
            if Table.compare(object_to_compare, query):
                filtered_objects.append(object_to_compare)
        return filtered_objects

    def __get_rows__(self, primary_keys):
        if primary_keys is None or len(primary_keys) == 0:
            raise WrongParameterError("No attributes found")
        rows = []
        for primary_key in primary_keys:
            rows.append(self.get_by_primary_key(str(primary_key)))
        return rows

    def __get_primary_key_path__(self, primary_key):
        path = os.path.join(self.__get_data_path__(), "{}.json".format(primary_key))
        if os.path.isfile(primary_key):
            return path
        return None

    def __get_primary_key_from_path__(self, path):
        return str(path).replace(self.__path__, '').replace(".json", '').replace("data", '')

    @staticmethod
    def compare(object_1, object_2):
        for attribute in object_2.items():
            if not object_1 or attribute[1] != object_1[attribute[0]]:
                return False
        return True

    def __get_data_path__(self):
        return os.path.join(self.__path__, "data")
