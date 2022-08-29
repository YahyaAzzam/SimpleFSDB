import json
import os
from keys import *


def search(path, primary_key):
    y = False
    for r, d, f in os.walk(path):
        if primary_key in f:
            y = True
            break
    return y


def creates_dir(schema):
    x = json.load(open(schema, 'r'))
    p = os.path.join(os.getcwd(), x[keys().database])
    exists = True
    if not os.path.exists(p):
        exists = False
        os.mkdir(p)
        for i in x[keys().Tables]:
            d = os.path.join(p, i[keys().name])
            os.mkdir(d)
    else:
        for i in x[keys().Tables]:
            d = os.path.join(p, i[keys().name])
            if not os.path.exists(d):
                exists = False
                os.mkdir(d)
    return exists


def creates(schema, table, primary_key):
    f = open(schema, 'r')
    x = json.load(f)
    f.close()
    path = os.path.join(os.getcwd(), x[keys().database])
    if not os.path.exists(path):
        return False
    path = path + '\\' + table + '\\' + primary_key
    if not os.path.exists(path):
        f = open(path, 'w')
        f.write("{\n")
        i = 0
        for k in x[keys().Tables]:
            if k[keys().name] != table:
                i = i + 1
            else:
                break
        x = x[keys().Tables][i]
        i = len(x[keys().columns])
        j = 0
        for t in x[keys().columns]:
            f.write("\t\"" + t + "\" : \"0\"")
            j = j + 1
            if j < i:
                f.write(",\n")
        f.write("\n}\n")
        f.close()
        return 1
    else:
        return 2


def sets(database, table, primary_key, parameter, value):
    path = os.getcwd() + '\\' + database + '\\' + table + '\\' + primary_key
    x = gets(database, table, primary_key)
    if not x:
        creates('Check-in-schema.json', table, primary_key)
        f = open(path, 'r')
        x = json.load(f)
        f.close()

    i = 0
    k = 0
    for k in x:
        if k != parameter:
            i = i + 1
        else:
            break
    x[k] = value
    f = open(path, 'w')
    json.dump(x, f)
    f.close()


def gets(database, table, primary_key):
    path = os.getcwd() + '\\' + database + '\\' + table
    if search(path, primary_key):
        f = open(path + '\\' + primary_key, 'r')
        e = json.load(f)
        f.close()
        return e
    else:
        return False


def deletes(database, table, primary_key):
    path = os.getcwd() + '\\' + database + '\\' + table
    if search(path, primary_key):
        os.remove(path + '\\' + primary_key)
        return True
    else:
        return False
