import sys, os
import unittest

sys.path.append(str(os.path.dirname(os.getcwd())))
from Querio.lib.commands.command_factory import *


class Test(unittest.TestCase):
    schema_path = None
    SCHEMA_PATH = None

    @classmethod
    def setUpClass(cls):
        cls.SCHEMA_PATH = os.getcwd()
        cls.schema_path = os.path.join(cls.SCHEMA_PATH, "Check-in-schema.json")

        # Create the database schema once for the entire class
        CreateCommand(cls.schema_path).execute()

    @classmethod
    def tearDownClass(cls):
        # Perform cleanup after all test methods in the class if needed
        database_path = os.path.join(os.path.dirname(os.getcwd()), 'Querio', 'storage')
        if os.path.exists(database_path):
            shutil.rmtree(database_path)

    def test_wrong_input_database(self):
        # didn't enter database name
        try:
            ClearCommand(None).execute()
        except NoParameterError:
            pass

        # enter empty string as database name
        try:
            ClearCommand("").execute()
        except NoParameterError:
            pass

        # enter space as database name
        try:
            ClearCommand(" ").execute()
        except WrongParameterError:
            pass

        # enter integers as database name
        try:
            ClearCommand("132654631").execute()
        except WrongParameterError:
            pass

        # enter wrong database name
        try:
            ClearCommand("goda").execute()
        except WrongParameterError:
            pass

    def test_clear(self):
        # tests clear database
        database = Database(database_name="csed25")
        ClearCommand("csed25").execute()

        for table in database.tables:
            # check data_dir is empty
            self.assertFalse(os.listdir(database.tables[table].get_data_path()))

            # check lock_dir is empty
            self.assertFalse(os.listdir(database.tables[table].get_lock_path()))

            # check data_dir is empty
            self.assertFalse(os.listdir(os.path.join(database.tables[table].get_path(), "indices")))


if __name__ == '__main__':
    unittest.main()
