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


def creates_dir(schema):
    data = json.load(open(schema, 'r'))
    path = os.path.join(os.getcwd(), data[keys().database])
    os.makedirs(path, exist_ok=True)

    for table in data[keys().Tables]:
        t_path = os.path.join(path, table[keys().name])
        os.makedirs(t_path, exist_ok=True)


def creates(schema, table, primary_key):
    file = open(schema, 'r')
    column = json.load(file)
    file.close()
    path = os.path.join(os.getcwd(), column[keys().database])
    if not os.path.exists(path):
        return False
    path = path + '\\' + table + '\\' + primary_key
    if not os.path.exists(path):
        json_object = {}
        file = open(path, 'w')
        index = 0
        for key in column[keys().Tables]:
            if key[keys().name] != table:
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


def sets(database, table, primary_key, parameter, value):
    path = os.getcwd() + '\\' + database + '\\' + table + '\\' + primary_key
    data = gets(database, table, primary_key)
    if not data:
        creates('Check-in-schema.json', table, primary_key)
        file = open(path, 'r')
        data = json.load(file)
        file.close()

    index = 0
    for index in data:
        if index == parameter:
            break
    data[index] = value
    file = open(path, 'w')
    json.dump(data, file)
    file.close()


def gets(database, table, primary_key):
    path = os.getcwd() + '\\' + database + '\\' + table
    if search(path, primary_key):
        file = open(path + '\\' + primary_key, 'r')
        json_object = json.load(file)
        file.close()
        return json_object
    else:
        return False


def deletes(database, table, primary_key):
    path = os.getcwd() + '\\' + database + '\\' + table
    if search(path, primary_key):
        os.remove(path + '\\' + primary_key)
        return True
    else:
        return False
