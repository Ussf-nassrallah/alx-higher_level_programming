#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle

""" Define a TestRectangle  Class """

class TestRectangleValues(unittest.TestCase):
    """ Test Rectangle arguments """
    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(5)
        with self.assertRaises(TypeError):
            Rectangle(None)
        with self.assertRaises(TypeError):
            Rectangle("string")
        with self.assertRaises(TypeError):
            Rectangle()

    def test_with_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_with_int(self):
        r_1 = Rectangle(10, 2)
        r_2 = Rectangle(2, 10)
        r_3 = Rectangle(5, 5)
        self.assertEqual(r_1.id, r_3.id - 2)

    def test_with_float(self):
        with self.assertRaises(TypeError):
            Rectangle(5.5, 2)
        with self.assertRaises(TypeError):
            Rectangle(5, 2.5)
        with self.assertRaises(TypeError):
            Rectangle(5.5, 2.5)

    def test_with_str(self):
        with self.assertRaises(TypeError):
            Rectangle("w", "h")
        with self.assertRaises(TypeError):
            Rectangle(100, "h")
        with self.assertRaises(TypeError):
            Rectangle("w", 100)

    def test_with_list(self):
        with self.assertRaises(TypeError):
            Rectangle([1, 2, 3], [1, 2, 3])
        with self.assertRaises(TypeError):
            Rectangle(100, [1, 2, 3])
        with self.assertRaises(TypeError):
            Rectangle([1, 2, 3], 100)

    def test_with_tuple(self):
        with self.assertRaises(TypeError):
            Rectangle((1, 2, 3), (1, 2, 3))
        with self.assertRaises(TypeError):
            Rectangle(100, (1, 2, 3))
        with self.assertRaises(TypeError):
            Rectangle((1, 2, 3), 100)

    def test_x_type(self):
        # while x -> None
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(100, 5, None)
        # while x -> None
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(100, 5, None, 10)
        # while x -> "string"
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(100, 5, "x", 10)
        # while x -> float
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(100, 5, 2.5, 10)
        # while x -> list
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(100, 5, [1, 2, 3], 10)
        # while x -> tuple
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(100, 5, (1, 2, 3), 10)

    def test_y_type(self):
        # while y -> None
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(100, 5, 2, None)
        # while y -> None
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(100, 5, 10, None)
        # while y -> "string"
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(100, 5, 10, "y")
        # while y -> float
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(100, 5, 2, 10.5)
        # while y -> list
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(100, 5, 1, [1, 2, 3])
        # while y -> tuple
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(100, 5, 1, (10, 11, 12))

    def test_x_value(self):
        # while x < 0
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(100, 5, -2, 3)

    def test_y_value(self):
        # while y < 0
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(100, 5, 2, -3)


class TestRectangleStrMethod(unittest.TestCase):
    """ Test Rectangle Str Method """
    def test_str_method_width_height_x(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)
