from command_factory import *
from ICommand import ICommand
from GetCommand import *
import json
import os
import keys



def create_files(schema, table, primary_key):
    file = open(schema, 'r')
    column = json.load(file)
    file.close()
    path = os.path.join(os.getcwd(), column[keys.DATABASE])
    if not os.path.exists(path):
        return "Database not found"
    path = os.path.join(path, table, primary_key)
    if not os.path.exists(path):
        file = open(path, 'w')
        for key in column[keys.TABLES]:
            if key[keys.NAME] == table:
                column = key
                break
        json.dump(write_table_schema(column[keys.COLUMNS]), file)
        file.close()



def write_table_schema(columns):
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
        if data == "Data not found":
            file = create_files('Check-in-schema.json', self.table, self.primary_key)
            if file == "Database not found":
                return file
            data = GetCommand(self.database, self.table, self.primary_key).execute()
        index = 0
        for index in data:
            if index == self.parameter:
                break

        data[index]=self.value
        file = open(path, 'w')
        json.dump(data, file)
        file.close()
        return "Data set successfully"
