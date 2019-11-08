# https://www.patricksoftwareblog.com/python-unit-testing-structuring-your-project/
#  python basicfunction.ut.py -v

import unittest
from basicfunction import BasicFunction
# import the class of interest (BasicFunction) from the basicfunction.py
# file
 
class TestBasicFunction(unittest.TestCase):
    def setUp(self):
        # setup() method to create a local instance of the class
        self.func = BasicFunction()
 
    def test_1(self):
        self.assertTrue(True)
 
    def test_2(self):
        self.assertTrue(True)
 
    def test_3(self):
        # unit test to check for initialization of local class
        self.assertEqual(self.func.state, 0)
 
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

