#!/usr/bin/python3


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    # Test Base class using None argument
    def test_with_none(self):
        obj1 = Base(None)
        obj2 = Base(None)
        obj3 = Base(None)
        self.assertEqual(obj1.id, obj3.id - 2)

    # Test Base class
    def test_global(self):
        obj1 = Base()
        obj2 = Base(12)
        obj3 = Base()

        self.assertEqual(obj1.id, obj3.id - 1)
        self.assertEqual(obj2.id, 12)


class TestBaseToJson(unittest.TestCase):
    """ test to_json_string static method """
    def test_to_json_zero_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_none_arg(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)



if __name__ == "__main__":
    unittest.main()
