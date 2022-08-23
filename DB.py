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
        "--data-base",
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
        "-v",
        "--value",
        type=str,
        help="Value desired to be set",
    )
    return parser.parse_args()


def create(schema):
    print(11)


args = parse_args()
args.command = input()
if args.command == "create":
    create(args.schema)
# elif args.command == "set":
#    set(args.database,args.table,args.primary_key,args.value)
# elif args.command == "get":
#    get(args.database,args.table,args.primary_key)
# elif args.command == "delete":
#    delete(args.database,args.table,args.primary_key)
