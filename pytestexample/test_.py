from SimpleFSDB.main import *
import unittest
import shutil


class Test(unittest.TestCase):

    def test_Create_with_cmd(self):
        # create the main dir and fix it if there is any problem using cmd
        os.system("main.py -c create -sc Check-in-schema.json")
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), "csed25")))

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

    def test_create_multiple_times(self):
        # create and delete database many times
        path = os.path.join(os.getcwd(), "csed25")
        shutil.rmtree(path)  # delete database
        for i in range(5):
            CreateCommand("Check-in-schema.json").execute()
            self.assertTrue(os.path.exists(path))
            shutil.rmtree(path)  # delete database

    def test_create_tables(self):
        # delete single table from database and then create it
        CreateCommand("Check-in-schema.json").execute()

        # delete Seats table
        path = os.path.join(os.getcwd(), "csed25", "Seats")
        shutil.rmtree(path)
        CreateCommand("Check-in-schema.json").execute()
        self.assertTrue(os.path.exists(path))

        # delete Reservations table
        path = os.path.join(os.getcwd(), "csed25", "Reservations")
        shutil.rmtree(path)
        CreateCommand("Check-in-schema.json").execute()
        self.assertTrue(os.path.exists(path))

        # delete Planes table
        path = os.path.join(os.getcwd(), "csed25", "Planes")
        shutil.rmtree(path)
        CreateCommand("Check-in-schema.json").execute()
        self.assertTrue(os.path.exists(path))

        # delete Flights table
        path = os.path.join(os.getcwd(), "csed25", "Flights")
        shutil.rmtree(path)
        CreateCommand("Check-in-schema.json").execute()
        self.assertTrue(os.path.exists(path))


if __name__ == '__main__':
    unittest.main()
