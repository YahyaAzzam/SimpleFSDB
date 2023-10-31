import unittest
from test_create import Test as TestCreate
from test_set import Test as TestSet
from test_delete import Test as TestDelete
from test_get import Test as TestGet
from test_clear import Test as TestClear

# Create a test suite to include all the test cases
test_suite = unittest.TestSuite()

# Add the test cases from each test class to the test suite
test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestCreate))
test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestSet))
test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDelete))
test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestGet))
test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestClear))

# Run the tests
if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite)

