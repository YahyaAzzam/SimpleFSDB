import sys, os
import unittest

sys.path.append(os.path.dirname(os.getcwd()))
from DataHive.lib.commands.command_factory import *
from DataHive.lib.model.schema_keys import Keys


class Test(unittest.TestCase):
    schema_name = "Check-in-schema.json"
    SCHEMA_PATH = os.getcwd()
    DATABASE_PATH = os.path.join(os.path.dirname(os.getcwd()), 'DataHive', 'storage')
    schema_path = os.path.join(SCHEMA_PATH, schema_name)
    file = open(schema_path, 'r')
    data = json.load(file)
    file.close()

    @classmethod
    def setUpClass(cls):
        # Create the database schema once for the entire class
        CreateCommand(cls.schema_path).execute()

    @classmethod
    def tearDownClass(cls):
        # Perform cleanup after all test methods in the class if needed
        if os.path.exists(cls.DATABASE_PATH):
            shutil.rmtree(cls.DATABASE_PATH)

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
        # create and delete the database many times
        path = os.path.join(self.DATABASE_PATH, self.data[Keys.DATABASE])
        if os.path.exists(path):
            shutil.rmtree(path)  # delete the database
        CreateCommand(os.path.join(self.SCHEMA_PATH, "Check-in-schema.json")).execute()
        self.assertTrue(os.path.exists(path))
        shutil.rmtree(path)  # delete the database

    def test_create_tables(self):
        # delete a single table from the database and then create it
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
        # check creating two JSON files in each table
        CreateCommand(os.path.join(self.SCHEMA_PATH, "Check-in-schema.json")).execute()

        for table in self.data[Keys.TABLES]:
            # check table_schema
            path = os.path.join(self.DATABASE_PATH, self.data[Keys.DATABASE], table[Keys.NAME])
            self.assertTrue(os.path.exists(os.path.join(path, table[Keys.NAME] + "_schema.json")))
            # check table_indices
            with open(os.path.join(path, table[Keys.NAME] + "_schema.json")) as file:
                table = json.load(file)
            for index in table[Keys.INDEX_KEYS]:
                if index != table[Keys.PRIMARY_KEY]:
                    self.assertTrue(os.path.exists(os.path.join(path, "indices", index)))


if __name__ == '__main__':
    unittest.main()
