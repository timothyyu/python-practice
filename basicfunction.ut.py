# https://www.patricksoftwareblog.com/python-unit-testing-structuring-your-project/
#  python basicfunction.ut.py -v

import unittest
from basicfunction import BasicFunction
# import the class of interest (BasicFunction) from the basicfunction.py
# file
 

# There's no explicit way to cause a test to "pass"
    # A test's status depends on the presence or absence of an exception
class TestBasicFunction(unittest.TestCase):
    def setUp(self):
        # setUp() method to create a local instance of the class

        # setUp() also used to establish test fixtures for all tests, i.e.
        # resources/libaries/connections and imports needed for said tests
            # setUp() to configure fixtures
            # tearDown() to clean up fixtures at end of unit test
        self.func = BasicFunction()

    # def test_fail(self):
    #     # desired outcome produces result that can be evaluated as false ---> use assertFalse()
    #     self.assertTrue(False,'failure message goes here - assertTrue is False for test_fail()')
 
    # def test_1(self):
    #     self.assertTrue(True)
 
    def test_2(self):
        # Case to check that class object state assignment is mutable with None assignment
        # upon new initialization of class obj
        self.func.state = None 
        self.assertIsNone(self.func.state,None)

    def test_3(self):
        # unit test to check for initialization of local class
        self.assertEqual(self.func.state, 0,'0-state init check - pass')
 
    def test_4(self):
        self.func.increment_state()
        self.assertEqual(self.func.state, 1)
 
    def test_5(self):
        self.func.increment_state()
        self.func.increment_state()
        self.func.clear_state()
        self.assertEqual(self.func.state, 0)

    def test_6(self):
        # Test case using both increment_state() and decrement_state() that should result in 2
        self.func.increment_state()
        self.func.increment_state()
        self.func.increment_state()
        self.func.decrement_state()
        self.assertEqual(self.func.state, 2)

if __name__ == '__main__':
    unittest.main(verbosity=3)
    # https://stackoverflow.com/a/1322648
        # verbosity = 0 ---> quiet, total numbers of tests executed and global result
        # verbosity = 1 ---> same as above with dot for every pass or F for every failed case
        # verbosity = 2 ---> full string output and result for every test

