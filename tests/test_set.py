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

    def test_wrong_input(self):
        SetCommand("csed25", "Seats", str({"FlightId_SeatId":"1","Last_name":"goda"})).execute()


        #path = database.get_path().replace("csed25", '')
        #if os.path.exists(path):
         #  shutil.rmtree(path)

if __name__ == '__main__':
    unittest.main()
