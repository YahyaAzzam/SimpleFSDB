import unittest
import shutil
import sys
import os
import json
sys.path.append(os.path.join(str(os.getcwd()).replace("tests", ''), "src"))
from commands.command_factory import *


class Test(unittest.TestCase):
    schema_name = "Check-in-schema.json"
    SCHEMA_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'tests', "Check-in-schema.json")
    DATABASE_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'tests', "csed25")
    CreateCommand(SCHEMA_PATH).execute()

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
    # test Get file in different tables
        database = Database(database_name = "csed25")

        for table in database.tables:
            table_mate_data = TableMetaData(database.tables[table])
            value = {}
            value[table_mate_data.primary_key] = "1"
            value[table_mate_data.columns[1]] = "goda"
            SetCommand("csed25", database.tables[table].get_name(), str(value)).execute()
            file = GetCommand("csed25", database.tables[table].get_name(), str(value)).execute()

            #check get file in the table
            self.assertEqual(file[0].data, value)

        # end the test and delete the database
        # delete database
        path = database.get_path().replace("csed25","")
        if os.path.exists(path):
            shutil.rmtree(path)


if __name__ == '__main__':
    unittest.main()
