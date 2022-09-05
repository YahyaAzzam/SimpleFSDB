import unittest
import shutil
import sys
import os
sys.path.append(os.path.join(str(os.getcwd()).replace("tests", ''), "src", "commands"))
from create_command import *


class Test(unittest.TestCase):
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
        path = os.path.join(str(os.getcwd()).replace("tests", ''), "tests", "csed25")
        if os.path.exists(path):
            shutil.rmtree(path)  # delete database
        CreateCommand("Check-in-schema.json").execute()
        self.assertTrue(os.path.exists(path))
        shutil.rmtree(path)  # delete database

    def test_create_tables(self):
        # delete single table from database and then create it
        CreateCommand("Check-in-schema.json").execute()

        # delete Seats table
        path = os.path.join(str(os.getcwd()).replace("tests", ''), "tests", "csed25", "Seats")
        shutil.rmtree(path)
        CreateCommand("Check-in-schema.json").execute()
        self.assertTrue(os.path.exists(path))

        # delete Reservations table
        path = os.path.join(str(os.getcwd()).replace("tests", ''), "tests", "csed25", "Reservations")
        shutil.rmtree(path)
        CreateCommand("Check-in-schema.json").execute()
        self.assertTrue(os.path.exists(path))

        # delete Planes table
        path = os.path.join(str(os.getcwd()).replace("tests", ''), "tests", "csed25", "Planes")
        shutil.rmtree(path)
        CreateCommand("Check-in-schema.json").execute()
        self.assertTrue(os.path.exists(path))

        # delete Flights table
        path = os.path.join(str(os.getcwd()).replace("tests", ''), "tests", "csed25", "Flights")
        shutil.rmtree(path)
        CreateCommand("Check-in-schema.json").execute()
        self.assertTrue(os.path.exists(path))
        shutil.rmtree(os.path.join(os.getcwd(), "csed25"))


if __name__ == '__main__':
    unittest.main()
