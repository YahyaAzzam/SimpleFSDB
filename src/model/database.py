from model.table import *


class Database:
    def __init__(self, obj):
        self.__validate__(obj)
        self.object = obj
        self.path = os.path.join(Keys.DATABASE_PATH, self.object[Keys.DATABASE])
        self.tables_objects = []
        for table in self.object[Keys.TABLES]:
            table_object = Table(self.object[Keys.DATABASE], table, self.path)
            self.tables_objects.append(table_object)

    def serialize(self):
        self.__create_database__()
        self.__create_tables__()

    @staticmethod
    def __validate__(obj):
        if len(obj[Keys.DATABASE]) == 0 or obj[Keys.DATABASE].isspace():
            raise WrongParameterError("No database detected")

    def __create_database__(self):
        os.makedirs(self.path, exist_ok=True)

    def __create_tables__(self):
        for table_object in self.tables_objects:
            table_object.serialize()
