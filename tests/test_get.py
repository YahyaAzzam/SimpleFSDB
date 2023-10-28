import sys, os
import unittest

sys.path.append(os.path.dirname(os.getcwd()))
from Querio.lib.commands.command_factory import *


class Test(unittest.TestCase):
    schema_name = "Check-in-schema.json"
    SCHEMA_PATH = os.getcwd()
    DATABASE_PATH = os.path.join(os.path.dirname(os.getcwd()), 'Querio', 'storage')
    schema_path = os.path.join(SCHEMA_PATH, schema_name)

    @classmethod
    def setUpClass(cls):
        # Create the database schema once for the entire class
        CreateCommand(cls.schema_path).execute()

    @classmethod
    def tearDownClass(cls):
        # Perform cleanup after all test methods in the class if needed
        if os.path.exists(cls.DATABASE_PATH):
            shutil.rmtree(cls.DATABASE_PATH)

    def test_wrong_get(self):
        try:  # No database entered
            GetCommand("", "Reservations", {"ReservationId": "552535"}).execute()
        except NoParameterError:
            pass
        try:  # No table entered
            GetCommand("csed", " ", {"ReservationId": "552535"}).execute()
        except NoParameterError:
            pass
        try:  # Wrong database name
            GetCommand("csed", "Reservations", "{\"ReservationId\": \"552535\"}").execute()
        except WrongParameterError:
            pass
        try:  # Wrong table name
            GetCommand("csed25", "Reservation", "{\"ReservationId\": \"552535\"}").execute()
        except WrongParameterError:
            pass
        try:  # Wrong database name
            GetCommand("csed25", "Reservations", "{\"ReservationId\": \"552535\"}").execute()
        except WrongParameterError:
            pass

    def test_Get(self):
        # tests Get file in different tables
        database = Database(database_name="csed25")

        for table in database.tables:
            table_mate_data = TableMetaData(database.tables[table])
            value = {table_mate_data.primary_key: "1", table_mate_data.columns[1]: "goda"}
            SetCommand("csed25", database.tables[table].get_name(), str(value)).execute()
            file = GetCommand("csed25", database.tables[table].get_name(), str(value)).execute()

            # check get file in the table
            self.assertEqual(file[0], value)


if __name__ == '__main__':
    unittest.main()
