import argparse
def parse_args():
    parser = argparse.ArgumentParser(description="Auto Sizer agent")
    parser.add_argument(
        '-c',
        "--command",
        type=str,
        help="The needed command to execute (create, get, set or delete)",
    )
    parser.add_argument(
        "-sc",
        "--schema_path",
        type=str,
        help="The path of the schema of the database, where the schema is a json object",
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
        "-q",
        "--query",
        type=str,
        help="Query desired to be found",
    )
    return parser.parse_args()
