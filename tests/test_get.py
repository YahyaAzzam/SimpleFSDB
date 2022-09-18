import unittest
import shutil
import sys
import os
import json
sys.path.append(os.path.join(str(os.getcwd()).replace("tests", ''), "src"))
from main import *


class Test(unittest.TestCase):
    schema_name = "Check-in-schema.json"
    SCHEMA_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'tests', "Check-in-schema.json")
    DATABASE_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'tests', "csed25")
    schema_path = os.path.join(SCHEMA_PATH, schema_name)
    file = open(schema_path, 'r')
    data = json.load(file)
    file.close()

    def test_wrong_get(self):
        if os.path.exists(self.DATABASE_PATH):
            shutil.rmtree(self.DATABASE_PATH)  # delete database
        CreateCommand(self.SCHEMA_PATH).execute()
        try:  # No database entered
            GetCommand("", "Reservations", {"ReservationId": "552535"})
        except NoParameterError:
            pass
        try:  # No table entered
            GetCommand("csed", " ", {"ReservationId": "552535"})
        except WrongParameterError:
            pass
        try:  # No values entered
            GetCommand("csed", "Reservations", None)
        except WrongParameterError:
            pass
        try:  # Wrong database name
            GetCommand("csed", "Reservations", {"ReservationId": "552535"})
        except WrongParameterError:
            pass
        try:  # Wrong table name
            GetCommand("csed25", "Reservation", {"ReservationId": "552535"})
        except WrongParameterError:
            pass
        try:  # Wrong database name
            GetCommand("csed25", "Reservations", {"ReservationId": "552535"})
        except WrongParameterError:
            pass


if __name__ == '__main__':
    unittest.main()
