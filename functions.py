import json
import os
from keys import *
from Command_factory import *
from ICommand import ICommand


def search(path, primary_key):
    found = False
    for roots, directories, files in os.walk(path):
        if primary_key in files:
            found = True
            break
    return found


class create_dir_command(ICommand):
    def __init__(self, schema):
        self.schema = schema

    def execute(self):
        data = json.load(open(self.schema, 'r'))
        path = os.path.join(os.getcwd(), data[keys().database])
        os.makedirs(path, exist_ok=True)

        for table in data[keys().Tables]:
            t_path = os.path.join(path, table[keys().name])
            os.makedirs(t_path, exist_ok=True)


class create_command(ICommand):
    def __init__(self, schema, table, primary_key):
        self.schema = schema
        self.table = table
        self.primary_key = primary_key

    def execute(self):
        file = open(self.schema, 'r')
        column = json.load(file)
        file.close()
        path = os.path.join(os.getcwd(), column[keys().database])
        if not os.path.exists(path):
            return False
        path = path + '\\' + self.table + '\\' + self.primary_key
        if not os.path.exists(path):
            json_object = {}
            file = open(path, 'w')
            index = 0
            for key in column[keys().Tables]:
                if key[keys().name] != self.table:
                    index = index + 1
                else:
                    column = column[keys().Tables][index]
                    break
            for element in column[keys().columns]:
                json_object[element] = '0'
            json.dump(json_object, file)
            file.close()
            return 1
        else:
            return 2


class set_command(ICommand):
    def __init__(self, database, table, primary_key, parameter, value):
        self.database = database
        self.table = table
        self.primary_key = primary_key
        self.parameter = parameter
        self.value = value

    def execute(self):
        path = os.getcwd() + '\\' + self.database + '\\' + self.table + '\\' + self.primary_key
        data = get_command(self.database, self.table, self.primary_key).execute()
        if not data:
            create_command('Check-in-schema.json', self.table, self.primary_key).execute()
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


class get_command(ICommand):

    def __init__(self, database, table, primary_key):
        self.database = database
        self.table = table
        self.primary_key = primary_key

    def execute(self):
        path = os.getcwd() + '\\' + self.database + '\\' + self.table
        if search(path, self.primary_key):
            file = open(path + '\\' + self.primary_key, 'r')
            json_object = json.load(file)
            file.close()
            return json_object
        else:
            return False


class delete_command(ICommand):

    def __init__(self, database, table, primary_key):
        self.database = database
        self.table = table
        self.primary_key = primary_key

    def execute(self):
        path = os.getcwd() + '\\' + self.database + '\\' + self.table
        if search(path, self.primary_key):
            os.remove(path + '\\' + self.primary_key)
            return True
        else:
            return False
