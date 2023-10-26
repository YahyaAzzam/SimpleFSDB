import sys, os
import unittest

sys.path.append(os.path.join(str(os.path.dirname(os.getcwd())), "Querio"))
from lib.commands.command_factory import *


class Test(unittest.TestCase):
    schema_name = "Check-in-schema.json"
    SCHEMA_PATH = os.getcwd()
    DATABASE_PATH = os.path.join(str(os.path.dirname(os.getcwd())), 'Querio', 'storage')
    schema_path = os.path.join(SCHEMA_PATH, schema_name)
    CreateCommand(schema_path).execute()

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

        # end the tests and delete the database
        # delete database
        path = database.get_path().replace("csed25", "")
        if os.path.exists(path):
            shutil.rmtree(path)


if __name__ == '__main__':
    unittest.main()
