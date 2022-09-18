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
    DATABASE_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'storage')
    schema_path = os.path.join(SCHEMA_PATH, schema_name)
    file = open(schema_path, 'r')
    data = json.load(file)
    file.close()

    def test_wrong_input(self):
        # didn't enter schema path
        try:
            CreateCommand(None).execute()
        except NoParameterError:
            pass

        # enter empty string as schema path
        try:
            CreateCommand("").execute()
        except NoParameterError:
            pass

        # enter space as schema path
        try:
            CreateCommand(" ").execute()
        except WrongParameterError:
            pass

        # enter space as schema name
        try:
            CreateCommand(os.path.join(self.SCHEMA_PATH, " ")).execute()
        except WrongParameterError:
            pass

        # enter integers as schema name
        try:
            CreateCommand(os.path.join(self.SCHEMA_PATH, "213313")).execute()
        except WrongParameterError:
            pass

        # enter wrong file name
        try:
            CreateCommand(os.path.join(self.SCHEMA_PATH, "goda")).execute()
        except WrongParameterError:
            pass

    def test_create(self):
        # create and delete database many times
        path = os.path.join(self.DATABASE_PATH, self.data[Keys.DATABASE])
        if os.path.exists(path):
            shutil.rmtree(path)  # delete database
        CreateCommand(os.path.join(self.SCHEMA_PATH, "Check-in-schema.json")).execute()
        self.assertTrue(os.path.exists(path))
        shutil.rmtree(path)  # delete database

    def test_create_tables(self):
        # delete single table from database and then create it
        CreateCommand(os.path.join(self.SCHEMA_PATH, "Check-in-schema.json")).execute()

        # delete each table in the database and recreate it
        for table in self.data[Keys.TABLES]:
            path = os.path.join(self.DATABASE_PATH, self.data[Keys.DATABASE], table[Keys.NAME])
            shutil.rmtree(path)
            CreateCommand(os.path.join(self.SCHEMA_PATH, "Check-in-schema.json")).execute()
            self.assertTrue(os.path.exists(path))
        path = os.path.join(self.DATABASE_PATH, self.data[Keys.DATABASE])
        if os.path.exists(path):
            shutil.rmtree(path)

    def test_create_tables_indices_file(self):
        # check creating two json files in each table
        CreateCommand(os.path.join(self.SCHEMA_PATH, "Check-in-schema.json")).execute()

        for table in self.data[Keys.TABLES]:
            # check table_schema
            path = os.path.join(self.DATABASE_PATH, self.data[Keys.DATABASE], table[Keys.NAME])
            self.assertTrue(os.path.exists(os.path.join(path, table[Keys.NAME] + "_schema.json")))
            # check table_indices
            with open(os.path.join(path, table[Keys.NAME] + "_schema.json")) as file:
                table = json.load(file)
            for index in table[Keys.INDEX_KEYS]:
                self.assertTrue(os.path.exists(os.path.join(path, index)))
        # delete database
        if os.path.exists(self.DATABASE_PATH):
            shutil.rmtree(self.DATABASE_PATH)


if __name__ == '__main__':
    unittest.main()
