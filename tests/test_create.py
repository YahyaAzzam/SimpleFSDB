import unittest
import shutil
import sys
import os

sys.path.append(os.path.join(str(os.getcwd()).replace("tests", ''), "src"))
from main import *


class Test(unittest.TestCase):
    schema_name = "Check-in-schema.json"
    path = os.path.join(Keys.SCHEMA_PATH, schema_name)
    file = open(path, 'r')
    data = json.load(file)
    file.close()

    def test_wrong_input(self):
        # didn't enter schema name
        try:
            CreateCommand(None).execute()
        except NoParameterError:
            pass

        # enter empty string as schema name
        try:
            CreateCommand("").execute()
        except NoParameterError:
            pass

        # enter space as schema name
        try:
            CreateCommand(" ").execute()
        except NoParameterError:
            pass

        # enter integers as schema name
        try:
            CreateCommand(2131131).execute()
        except WrongParameterError:
            pass

        # enter wrong file name
        try:
            CreateCommand("goda").execute()
        except WrongParameterError:
            pass

    def test_create(self):
        # create and delete database many times
        path = os.path.join(Keys.DATABASE_PATH, self.data[Keys.DATABASE])
        if os.path.exists(path):
            shutil.rmtree(path)  # delete database
        CreateCommand(self.schema_name).execute()
        self.assertTrue(os.path.exists(path))
        shutil.rmtree(path)  # delete database

    def test_create_tables(self):
        # delete single table from database and then create it
        CreateCommand(self.schema_name).execute()

        # delete each table in the database and recreate it
        for table in self.data[Keys.TABLES]:
            path = os.path.join(Keys.DATABASE_PATH, self.data[Keys.DATABASE], table[Keys.NAME])
            shutil.rmtree(path)
            CreateCommand(self.schema_name).execute()
            self.assertTrue(os.path.exists(path))
        path = os.path.join(Keys.DATABASE_PATH, self.data[Keys.DATABASE])
        if os.path.exists(path):
            shutil.rmtree(path)

    def test_create_tables_indices_file(self):
        # check creating two json files in each table
        CreateCommand(self.schema_name).execute()

        for table in self.data[Keys.TABLES]:
            # check table_schema
            path = os.path.join(Keys.DATABASE_PATH, self.data[Keys.DATABASE], table[Keys.NAME],
                                table[Keys.NAME] + "_schema.json")
            self.assertTrue(os.path.exists(path))
            # check table_indices
            # path = os.path.join(Keys.DATABASE_PATH, self.data[Keys.DATABASE], table[Keys.NAME],
            #                     table[Keys.NAME] + "_indices.json")
            # self.assertTrue(os.path.exists(path))
        # delete database
        path = os.path.join(Keys.DATABASE_PATH, self.data[Keys.DATABASE])
        if os.path.exists(path):
            shutil.rmtree(path)


if __name__ == '__main__':
    unittest.main()
