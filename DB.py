import argparse
import json
import os


def parse_args():
    parser = argparse.ArgumentParser(description="Auto Sizer agent")
    parser.add_argument(
        "-c",
        "--command",
        type=str,
        help="The needed command to execute (create, get, set or delete)",
    )
    parser.add_argument(
        "-sc",
        "--schema",
        type=str,
        help="The schema of the database, which is a json object",
    )
    parser.add_argument(
        "-db",
        "--database",
        type=str,
        help="The database where the data wanted is stored",
    )
    parser.add_argument(
        "-t",
        "--table",
        type=str,
        help="Specific table in a database",
    )
    parser.add_argument(
        "-pk",
        "--primary-key",
        type=str,
        help="Primary key is a unique key",
    )
    parser.add_argument(
        "-p",
        "--parameter",
        type=str,
        help="Parameter desired to be set",
    )
    parser.add_argument(
        "-v",
        "--value",
        type=str,
        help="Value of the parameter",
    )
    return parser.parse_args()


def search(path, primary_key):
    y = False
    for f in os.walk(path):
        if primary_key in f:
            y = True
            break
    return y


def creates(schema):
    x = json.load(open(schema, 'r'))
    p = os.path.join(os.getcwd(), x['database_name'])
    os.mkdir(p)
    for i in x['Tables']:
        d = os.path.join(p, i['name'])
        os.mkdir(d)


def sets(database, table, primary_key, parameter, value):
    x = gets(database, table, primary_key)
    if x == "Error":
        return x
    else:
        x[parameter] = value
        return True


def gets(database, table, primary_key):
    path = os.getcwd() + '\\' + database + '\\' + table
    if search(path, primary_key):
        return json.load(open(path + '\\' + primary_key, 'r'))
    else:
        return "Error"


def deletes(database, table, primary_key):
    path = os.getcwd() + '\\' + database + '\\' + table
    if search(path, primary_key):
        os.remove(path + '\\' + primary_key)
        return True
    else:
        return "Error"


args = parse_args()
if args.command == "create":
    creates(args.schema)
elif args.command == "set":
    m = sets(args.database, args.table, args.primary_key, args.parameter, args.value)
    if "Error" == m:
        print(m)
elif args.command == "get":
    m = gets(args.database, args.table, args.primary_key)
    if "Error" == m:
        print(m)
elif args.command == "delete":
    m = deletes(args.database, args.table, args.primary_key)
    if "Error" == m:
        print(m)
