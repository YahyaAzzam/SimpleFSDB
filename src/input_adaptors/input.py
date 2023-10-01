# Import the argparse module for parsing command-line arguments
import argparse

# Define a function called parse_args() for parsing command-line arguments
def parse_args():
    # Create an ArgumentParser object with a description
    parser = argparse.ArgumentParser(description="Database management system")

    # Define command-line arguments and their types, as well as help messages
    parser.add_argument(
        '-c',
        "--command",
        type=str,
        help="The operation to perform on the database (create, get, set, or delete)."
    )
    parser.add_argument(
        "-sc",
        "--schema_path",
        type=str,
        help="The path to the JSON schema file defining the database structure."
    )
    parser.add_argument(
        "-db",
        "--database",
        type=str,
        help="The name of the database where the data is stored."
    )
    parser.add_argument(
        "-t",
        "--table",
        type=str,
        help="The name of the specific table in the database."
    )
    parser.add_argument(
        "-q",
        "--query",
        type=str,
        help="The query string to filter data when using 'get' or 'delete' operations."
    )

    # Parse the command-line arguments and return the result
    return parser.parse_args()
