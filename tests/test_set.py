import sys, os
import unittest

sys.path.append(os.path.dirname(os.getcwd()))
from Querio.lib.commands.command_factory import *


class Test(unittest.TestCase):
    SCHEMA_PATH = os.getcwd()
    schema_name = "Check-in-schema.json"

    @classmethod
    def setUpClass(cls):
        # Create the database schema once for the entire class
        schema_path = os.path.join(cls.SCHEMA_PATH, cls.schema_name)
        CreateCommand(schema_path).execute()

    @classmethod
    def tearDownClass(cls):
        # Perform cleanup after all test methods in the class if needed
        DATABASE_PATH = os.path.join(os.path.dirname(os.getcwd()), 'Querio', 'storage')
        if os.path.exists(DATABASE_PATH):
            shutil.rmtree(DATABASE_PATH)

    def test_wrong_input_database(self):
        # didn't enter database name
        try:
            SetCommand(None, "Seats", str({"FlightId_SeatId": "1", "Last_name": "goda"})).execute()
        except NoParameterError:
            pass

        # enter empty string as database name
        try:
            SetCommand("", "Seats", str({"FlightId_SeatId": "1", "Last_name": "goda"})).execute()
        except NoParameterError:
            pass

        # enter space as database name
        try:
            SetCommand(" ", "Seats", str({"FlightId_SeatId": "1", "Last_name": "goda"})).execute()
        except WrongParameterError:
            pass

        # enter integers as database name
        try:
            SetCommand("132654631", "Seats", str({"FlightId_SeatId": "1", "Last_name": "goda"})).execute()
        except WrongParameterError:
            pass

        # enter wrong database name
        try:
            SetCommand("goda", "Seats", str({"FlightId_SeatId": "1", "Last_name": "goda"})).execute()
        except WrongParameterError:
            pass

    def test_wrong_input_table(self):
        # enter None as table name
        try:
            SetCommand("csed25", None, str({"FlightId_SeatId": "1", "Last_name": "goda"})).execute()
        except WrongParameterError:
            pass

        # enter empty string as table name
        try:
            SetCommand("csed25", "", str({"FlightId_SeatId": "1", "Last_name": "goda"})).execute()
        except WrongParameterError:
            pass

        # enter space as table name
        try:
            SetCommand("csed25", " ", str({"FlightId_SeatId": "1", "Last_name": "goda"})).execute()
        except WrongParameterError:
            pass

        # enter integers as table name
        try:
            SetCommand("csed25", "654646422", str({"FlightId_SeatId": "1", "Last_name": "goda"})).execute()
        except WrongParameterError:
            pass

        # enter wrong table name
        try:
            SetCommand("csed25", "goda", str({"FlightId_SeatId": "1", "Last_name": "goda"})).execute()
        except WrongParameterError:
            pass

    def test_set(self):
        # tests set file in different tables
        database = Database(database_name="csed25")

        for table in database.tables:
            table_mate_data = TableMetaData(database.tables[table])
            value = {table_mate_data.primary_key: "1", table_mate_data.columns[1]: "goda"}
            SetCommand("csed25", database.tables[table].get_name(), str(value)).execute()

            # check create the file in the table
            self.assertTrue(os.path.exists(os.path.join(database.tables[table].get_data_path(), "1.json")))

            # check blocking reset file
            if table_mate_data.overwrite == "False":
                with self.assertRaises(OverwriteError):
                    SetCommand("csed25", database.tables[table].get_name(), str(value)).execute()

            # create file without passing the primary_key
            try:
                SetCommand("csed25", database.tables[table].get_name(), str({"Last_name": "goda"})).execute()
            except Exception:
                self.assertTrue(False)

            # check reset file with new value
            if table_mate_data.overwrite == "True":
                value[table_mate_data.columns[1]] = "mahmoud"
                SetCommand("csed25", database.tables[table].get_name(), str(value)).execute()
                self.assertEqual(database.tables[table].get_by_primary_key(1).get_data(), value)


if __name__ == '__main__':
    unittest.main()
