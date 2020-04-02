import unittest
from UI.tests.basic_test import BasicTest

def full_suite():
    test_suite = unittest.TestSuite()
    # adding test classes
    test_suite.addTest(unittest.makeSuite(BasicTest))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(full_suite())
