#!/usr/bin/python3


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    # Test Base class using zero arguments
    def test_no_args(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()

        self.assertEqual(obj1.id, obj3.id - 2)

    # Test Base class using arguments
    def test_with_args(self):
        obj1 = Base(12)
        obj2 = Base(13)
        obj3 = Base(14)

        self.assertEqual(obj1.id, 12)
        self.assertEqual(obj2.id, 13)
        self.assertEqual(obj3.id, 14)

    # Test Base class
    def test_global(self):
        obj1 = Base()
        obj2 = Base(12)
        obj3 = Base()

        self.assertEqual(obj1.id, obj3.id - 1)
        self.assertEqual(obj2.id, 12)

if __name__ == "__main__":
    unittest.main()
