from main import *
import unittest



class Test(unittest.TestCase):
    # create the main dir and fix it if there is any problem
    os.system("main.py -c create -sc Check-in-schema.json")

    def test_get(self):
        # create json file in seats table then get data from it
        create_files("Check-in-schema.json", "Seats", "1.json")
        x = GetCommand("csed25", "Seats", "1.json").execute()
        ans = {'Last_name': '0', 'ReservationId': '0'}
        self.assertEqual(x, ans)

    def test_get_nothing(self):
        # get data from json file, but I didn't create this file
        x = GetCommand("csed25", "Seats", "2.json").execute()
        self.assertEqual(x, "Data not found")  # there is no json file so it return False

    def test_set(self):
        # set the last name in the json file to(goda) and the id to(123)
        SetCommand("csed25", "Seats", "1.json", "Last_name", "goda").execute()
        SetCommand("csed25", "Seats", "1.json", "ReservationId", "123").execute()
        x = GetCommand("csed25", "Seats", "1.json").execute()
        ans = {'Last_name': 'goda', 'ReservationId': '123'}
        self.assertEqual(x, ans)

    def test_set_NewFile(self):
        # set the value in uncreated file to(goda) and(123) this will create the file with the given values
        SetCommand("csed25", "Seats", "2.json", "Last_name", "goda").execute()
        SetCommand("csed25", "Seats", "2.json", "ReservationId", "123").execute()
        x = GetCommand("csed25", "Seats", "2.json").execute()
        ans = {'Last_name': 'goda', 'ReservationId': '123'}
        self.assertEqual(x, ans)

    def test_deleteFiles(self):
        # delete all the created files
        DeleteCommand("csed25", "Seats", "1.json").execute()
        DeleteCommand("csed25", "Seats", "2.json").execute()
        path1 = os.path.join(os.getcwd(), "csed25", "Seats", "1.json")
        path2 = os.path.join(os.getcwd(), "csed25", "Seats", "2.json")
        self.assertEqual(os.path.exists(path1) or os.path.exists(path2), False)


if __name__ == '__main__':
    unittest.main()
