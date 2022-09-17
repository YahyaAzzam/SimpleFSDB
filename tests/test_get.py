import unittest
import shutil
import sys
import os
import json
sys.path.append(os.path.join(str(os.getcwd()).replace("tests", ''), "src"))
from main import *


class Test(unittest.TestCase):
    schema_name = "Check-in-schema.json"
    SCHEMA_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'tests')
    DATABASE_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'tests')
    schema_path = os.path.join(SCHEMA_PATH, schema_name)
    file = open(schema_path, 'r')
    data = json.load(file)
    file.close()
    # tests will be implemented later


if __name__ == '__main__':
    unittest.main()
