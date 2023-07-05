#!/usr/bin/python3
""" define TestMaxInteger Class """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ represent TestMaxInteger """
    def test_max_integer(self):
        self.assertEquals(max_integer([1, 2, 3, 4]), 4)
        self.assertEquals(max_integer([-1, -2, -3, 0]), 0)
        self.assertEquals(max_integer([-4, -3, -2, -1]), -1)
        self.assertEquals(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
