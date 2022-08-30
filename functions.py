from command_factory import *
from ICommand import ICommand
import json
import os
from keys import *


def search(path, primary_key):
    found = False
    for roots, directories, files in os.walk(path):
        if primary_key in files:
            found = True
            break
    return found


class CreateDirCommand(ICommand):
    def __init__(self, schema):
        self.schema = schema

    def execute(self):
        if self.schema is None:
            return "Schema not found"
        data = json.load(open(self.schema, 'r'))
        path = os.path.join(os.getcwd(), data[Keys().DATABASE])
        os.makedirs(path, exist_ok=True)
        for table in data[Keys().TABLES]:
            t_path = os.path.join(path, table[Keys().NAME])
            os.makedirs(t_path, exist_ok=True)
        return "Database created successfully"


class CreateCommand(ICommand):
    def __init__(self, schema, table, primary_key):
        self.schema = schema
        self.table = table
        self.primary_key = primary_key

    def execute(self):
        if self.schema is None:
            return "Schema not found"
        if self.table is None:
            return "Table not found"
        if self.primary_key is None:
            return "Primary key not found"
        file = open(self.schema, 'r')
        column = json.load(file)
        file.close()
        path = os.path.join(os.getcwd(), column[Keys().DATABASE])
        if not os.path.exists(path):
            return "Database not found"
        path = path + '\\' + self.table + '\\' + self.primary_key
        if not os.path.exists(path):
            file = open(path, 'w')
            index = 0
            for key in column[Keys().TABLES]:
                if key[Keys().NAME] != self.table:
                    index = index + 1
                else:
                    column = column[Keys().TABLES][index]
                    break
            json.dump(self.__write_table_schema(column[Keys.COLUMNS]), file)
            file.close()
            return "Column created successfully"
        else:
            return "Column already found"

    @staticmethod
    def __write_table_schema(columns):
        json_object = {}
        for element in columns:
            json_object[element] = '0'
        return json_object


class SetCommand(ICommand):
    def __init__(self, database, table, primary_key, parameter, value):
        self.database = database
        self.table = table
        self.primary_key = primary_key
        self.parameter = parameter
        self.value = value

    def execute(self):
        if self.database is None:
            return "Database not found"
        if self.table is None:
            return "Table not found"
        if self.primary_key is None:
            return "Primary key not found"
        if self.parameter is None:
            return "Parameter not found"
        if self.value is None:
            return "Value not found"
        path = os.path.join(os.getcwd(), self.database, self.table, self.primary_key)
        data = GetCommand(self.database, self.table, self.primary_key).execute()
        if not data:
            CreateCommand('Check-in-schema.json', self.table, self.primary_key).execute()
            file = open(path, 'r')
            data = json.load(file)
            file.close()
        index = 0
        for index in data:
            if index == self.parameter:
                break
        data[index] = self.value
        file = open(path, 'w')
        json.dump(data, file)
        file.close()
        return "Data set successfully"


class GetCommand(ICommand):

    def __init__(self, database, table, primary_key):
        self.database = database
        self.table = table
        self.primary_key = primary_key

    def execute(self):
        if self.database is None:
            return "Database not found"
        if self.table is None:
            return "Table not found"
        if self.primary_key is None:
            return "Primary key not found"
        path = os.path.join(os.getcwd(), self.database, self.table)
        if search(path, self.primary_key):
            file = open(path + '\\' + self.primary_key, 'r')
            json_object = json.load(file)
            file.close()
            return json_object
        else:
            return "Data not found"


class DeleteCommand(ICommand):

    def __init__(self, database, table, primary_key):
        self.database = database
        self.table = table
        self.primary_key = primary_key

    def execute(self):
        if self.database is None:
            return "Database not found"
        if self.table is None:
            return "Table not found"
        if self.primary_key is None:
            return "Primary key not found"
        path = os.path.join(os.getcwd(), self.database, self.table)
        if search(path, self.primary_key):
            os.remove(os.path.join(path, self.primary_key))
            return "Data deleted successfully"
        else:
            return "Data not found"
