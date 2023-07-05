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

        self.assertEquals(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEquals(max_integer([-1.5, -2.5, -3.5, 0]), 0)
        self.assertEquals(max_integer([-4.5, -3.5, -2.5, -1.5]), -1.5)

        self.assertEquals(max_integer([1.5, 2, 3.5, 4]), 4)
        self.assertEquals(max_integer([4, 3, 2, 1]), 4)
        self.assertEquals(max_integer([-1, -2, 3, -4]), 3)

        self.assertEquals(max_integer(["a", "b", "c", "d"]), "d")
        self.assertEquals(max_integer(["z", "e", "f", "h"]), "z")
        self.assertEquals(max_integer("abcd"), "d")

        self.assertEquals(max_integer([5]), 5)
        self.assertEquals(max_integer([-2]), -2)
        self.assertEquals(max_integer([0]), 0)

        self.assertEquals(max_integer(""), None)
        self.assertEquals(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
