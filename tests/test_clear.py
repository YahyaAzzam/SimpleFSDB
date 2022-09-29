import unittest
import shutil
import os
import json
import sys
sys.path.append(os.path.join(str(os.getcwd()).replace("tests", ''), "src"))
from commands.command_factory import *


class Test(unittest.TestCase):
    SCHEMA_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'tests')
    CreateCommand(os.path.join(SCHEMA_PATH, "Check-in-schema.json")).execute()

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
        # test clear database
        database = Database(database_name = "csed25")
        ClearCommand("csed25").execute()

        for table in database.tables:
            # check data_dir is empty
            self.assertFalse(os.listdir(database.tables[table].get_data_path()))

            # check lock_dir is empty
            self.assertFalse(os.listdir(database.tables[table].get_lock_path()))

            # check data_dir is empty
            self.assertFalse(os.listdir(os.path.join(database.tables[table].get_path(), "indices")))

        # end the test and delete the database
        # delete database
        path = database.get_path().replace("csed25","")
        if os.path.exists(path):
            shutil.rmtree(path)


if __name__ == '__main__':
    unittest.main()