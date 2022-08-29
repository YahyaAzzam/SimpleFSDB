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
        help="Parameters desired to be set as a json object",
    )
    parser.add_argument(
        "-v",
        "--values",
        type=str,
        help="Values of the parameters as a json object",
    )
    return parser.parse_args()
