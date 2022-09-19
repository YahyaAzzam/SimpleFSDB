import unittest
import shutil
import sys
import os
import json
sys.path.append(os.path.join(str(os.getcwd()).replace("tests", ''), "src"))
from main import *


class Test(unittest.TestCase):
    SCHEMA_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'tests')
    CreateCommand(os.path.join(SCHEMA_PATH, "Check-in-schema.json")).execute()

    def test_wrong_input_database(self):
        # didn't enter database name
        try:
            SetCommand(None, "Seats", str({"FlightId_SeatId":"1","Last_name":"goda"})).execute()
        except NoParameterError:
            pass

        # enter empty string as database name
        try:
            SetCommand("", "Seats", str({"FlightId_SeatId":"1","Last_name":"goda"})).execute()
        except NoParameterError:
            pass

        # enter space as database name
        try:
            SetCommand(" ", "Seats", str({"FlightId_SeatId":"1","Last_name":"goda"})).execute()
        except WrongParameterError:
            pass

        # enter integers as database name
        try:
            SetCommand("132654631", "Seats", str({"FlightId_SeatId":"1","Last_name":"goda"})).execute()
        except WrongParameterError:
            pass

        # enter wrong database name
        try:
            SetCommand("goda", "Seats", str({"FlightId_SeatId":"1","Last_name":"goda"})).execute()
        except WrongParameterError:
            pass

    def test_wrong_input_table(self):
        # didn't enter table name
        try:
            SetCommand("csed25", None, str({"FlightId_SeatId":"1","Last_name":"goda"})).execute()
        except NoParameterError:
            pass

        # enter empty string as table name
        try:
            SetCommand("csed25", "", str({"FlightId_SeatId":"1","Last_name":"goda"})).execute()
        except NoParameterError:
            pass

        # enter space as table name
        try:
            SetCommand("csed25", " ", str({"FlightId_SeatId":"1","Last_name":"goda"})).execute()
        except WrongParameterError:
            pass

        # enter integers as table name
        try:
            SetCommand("csed25", "654646422", str({"FlightId_SeatId":"1","Last_name":"goda"})).execute()
        except WrongParameterError:
            pass

        # enter wrong table name
        try:
            SetCommand("csed25", "goda", str({"FlightId_SeatId":"1","Last_name":"goda"})).execute()
        except WrongParameterError:
            pass

    def test_wrong_input_file(self):
        # didn't enter file name
        try:
            SetCommand("csed25", "Seats", None).execute()
        except NoParameterError:
            pass

        # enter empty string as file name
        try:
            SetCommand("csed25", "Seats", "").execute()
        except NoParameterError:
            pass

        # enter space as file name
        try:
            SetCommand("csed25", "Seats", " ").execute()
        except WrongParameterError:
            pass

        # enter integers as file name
        try:
            SetCommand("csed25", "Seats", "123451").execute()
        except WrongParameterError:
            pass

        # enter wrong file name
        try:
            SetCommand("csed25", "Seats", "goda").execute()
        except WrongParameterError:
            pass

    def test_set(self):
        # test set file in different tables
        database = Database(database_name = "csed25")
        for table in database.tables:
            table_mate_data = TableMetaData(database.tables[table])
            value = {}
            value[table_mate_data.primary_key] = "1"
            value[table_mate_data.columns[1]] = "goda"
            SetCommand("csed25", database.tables[table].get_name(), str(value)).execute()

            #check create the file in the table
            self.assertTrue(os.path.exists(os.path.join(table_mate_data.get_path(),"1.json")))

            #check blocking reset file
            try:
                SetCommand("csed25", database.tables[table].get_name(), str(value)).execute()
            except WrongParameterError:
                pass

            #check reset file with new value
            if database.tables[table].get_name() == "Seats":
                value[table_mate_data.columns[1]] = "mahmoud"
                SetCommand("csed25", database.tables[table].get_name(), str(value)).execute()
                self.assertEqual(database.tables[table].get_by_primary_key(1),value)

        # end the test and delete the database
        path = database.get_path().replace("csed25", '')
        if os.path.exists(path):
           shutil.rmtree(path)


if __name__ == '__main__':
    unittest.main()
