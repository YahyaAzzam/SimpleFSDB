import unittest
import shutil
from Functions.create_command import *


class Test(unittest.TestCase):

    def test_wrong_input(self):
        # didn't enter schema name
        status = CreateCommand(None).execute()
        self.assertEqual(status, 3)

        # enter empty string as schema name
        status = CreateCommand("").execute()
        self.assertEqual(status, 3)

        # enter space as schema name
        CreateCommand(" ").execute()
        self.assertEqual(status, 3)

        # enter integers as schema name
        CreateCommand(2131131).execute()
        self.assertEqual(status, 4)

        # enter wrong file name
        CreateCommand("goda").execute()
        self.assertEqual(status, 4)

    def test_create_multiple_times(self):
        # create and delete database many times
        path = os.path.join(os.getcwd(), "csed25")
        if os.path.exists(path):
            shutil.rmtree(path)  # delete database
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
