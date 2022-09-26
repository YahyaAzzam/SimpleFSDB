from model.table_metadata import *
from model.row import *
import shutil


class Table:
    def __init__(self, database,  table_name, table_schema = None):
        self.__path__ = os.path.join(database.get_path(), table_name)
        if table_schema is None:
            table_schema = TableMetaData.load_table_schema(self.__path__, table_name)
        self.table_schema = table_schema
        self.__table_metadata__ = TableMetaData(self)

    def serialize(self):
        os.makedirs(os.path.join(self.get_data_path(), "Lock"), exist_ok=True)
        self.__table_metadata__.serialize()

    def get_name(self):
        return self.__table_metadata__.name

    def get_path(self):
        return self.__path__

    def get_data_path(self):
        return os.path.join(self.__path__, "data")
        
    def get_primary_key(self):
        return self.__table_metadata__.primary_key

    def can_overwrite(self):
        return eval(self.__table_metadata__.overwrite)

    def get_indices(self):
        return self.__table_metadata__.index_keys

    def set(self, data):
        primary_key = data.get(self.get_primary_key())
        existing_row = self.get_by_primary_key(primary_key) if primary_key else None
        row = Row(self, data)
        if not self.can_overwrite() and row.row_exists():
            raise OverwriteError("data exists")
        existing_row.delete() if existing_row else None
        row.serialize()

    def delete(self, query):
        rows = self.get(query)
        for row in rows:
            row.delete()
            pathlib.Path(row.get_row_path()).unlink()

    def get(self, query):
        efficient_index = self.__get_efficient_index__(query)
        if efficient_index is None:
            efficient_keys = self.__get_all_primary_keys__()
        else:
            efficient_keys = efficient_index.get_primary_keys(query[efficient_index])
        found_objects = self.__get_rows__(efficient_keys)
        return self.__filter_by_query__(found_objects, query)

    def __get_efficient_index__(self, query):
        if not query or str(query).isspace:
            return None
        efficient_value = None
        for index_name in query.keys():
            current_index = self.__table_metadata__.get_index(index_name)
            current_value = current_index.get_index_value(query[index_name])
            if current_index and (not efficient_value or current_value.compare(efficient_value)) > 0:
                efficient_value = current_value
        return efficient_value.get_index()

    def __get_all_primary_keys__(self):
        primary_keys = []
        for primary_key in os.listdir(self.get_data_path()):
            if primary_key != "Lock":
                primary_keys.append(primary_key.replace(".json",""))
        return primary_keys

    def get_by_primary_key(self, primary_key):
        return Row.load_by_primary_key(self, primary_key)

    @staticmethod
    def __filter_by_query__(found_objects, query):
        if not query or str(query).isspace():
            return found_objects
        filtered_objects = []
        for object_to_compare in found_objects:
            if object_to_compare and object_to_compare.compare(query):
                filtered_objects.append(object_to_compare)
        return filtered_objects

    def __get_rows__(self, primary_keys):
        rows = []
        for primary_key in primary_keys:
            rows.append(self.get_by_primary_key(str(primary_key)))
        return rows

    def clear(self):
        for table_element in os.listdir(self.__path__):
            path = os.path.join(self.__path__, table_element)
            if os.path.isdir(path):
                shutil.rmtree(path)
                os.mkdir(path)

    @staticmethod
    def compare(object_1, object_2):
        for attribute in object_2.items():
            if not object_1 or attribute[1] != object_1[attribute[0]]:
                return False
        return True
