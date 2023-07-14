#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    # Test Using zero arguments
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
