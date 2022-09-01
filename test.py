from main import *
import unittest



class Test(unittest.TestCase):

    def test_Create_with_cmd(self):
        #create the main dir and fix it if there is any problem using cmd
        os.system("main.py -c create -sc Check-in-schema.json")
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), "csed25")))

    def test_wrong_input(self):
        output="Schema not found"
        #didn't enter schema name
        self.assertEqual(CreateCommand(None).execute(),output)

        #enter empty string as schema name
        self.assertEqual(CreateCommand("").execute(),output)

        #enter space as schema name
        self.assertEqual(CreateCommand(" ").execute(),output)

        #enter integers as schema name
        self.assertEqual(CreateCommand(2131131).execute(),output)

        #enter wrong file name
        self.assertEqual(CreateCommand("goda").execute(),output)

    def test_create_multiple_times(self):
        path=os.path.join(os.getcwd(), "csed25")
        os.remove(path)
        for i in range(5):
            CreateCommand("Check-in-schema.json").execute()
            self.assertEqual(os.path.exists(path), True)




if __name__ == '__main__':
    unittest.main()
