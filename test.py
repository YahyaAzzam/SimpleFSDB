from main import *
import unittest



class Test(unittest.TestCase):
#create the main dir and fix it if there is any problem
    os.system("main.py -c create_dir -sc Check-in-schema.json")
    def test_get(self):
        #create json file in seats table then get data from it
        os.system("main.py -c create -sc Check-in-schema.json -t Seats -pk 1.json")
        x=gets("csed25","Seats","1.json")
        ans={'Last_name': '0', 'ReservationId': '0'}
        self.assertEqual(x,ans)
    def test_get_nothing(self):
        #get data from json file but i didn't create this file
        x=gets("csed25","Seats","2.json")
        self.assertEqual(x,False)# there is no json file so it return False
    def test_set(self):
        #set the last name in the json file to(goda) and the id to(123)
        sets("csed25","Seats","1.json","Last_name","goda")
        sets("csed25","Seats","1.json","ReservationId","123")
        x=gets("csed25","Seats","1.json")
        ans={'Last_name': 'goda', 'ReservationId': '123'}
        self.assertEqual(x,ans)
    def test_set_NewFile(self):
        #set the value in uncreated file to(goda) and(123) this will create the file with the given values
        sets("csed25","Seats","2.json","Last_name","goda")
        sets("csed25","Seats","2.json","ReservationId","123")
        x=gets("csed25","Seats","2.json")
        ans={'Last_name': 'goda', 'ReservationId': '123'}
        self.assertEqual(x,ans)
    def test_deleteFiles(self):
        #delete all the created files
        deletes("csed25","Seats","1.json")
        deletes("csed25","Seats","2.json")
        path1=path = os.getcwd() + '\\' + "csed25" + '\\' + "Seats" + '\\' + "1.json"
        path2=path = os.getcwd() + '\\' + "csed25" + '\\' + "Seats" + '\\' + "2.json"
        self.assertEqual(os.path.exists(path1) or os.path.exists(path2),False)
if __name__ == '__main__':
    unittest.main()
