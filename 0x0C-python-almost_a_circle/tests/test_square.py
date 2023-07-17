#!/usr/bin/python3

""" Define a TestSquare class for testing Square Class """

import sys
import io
import unittest
from models.square import Square
from models.base import Base


class TestSquareSize(unittest.TestCase):
    """ test sqaure: size argument """
    def test_no_argument(self):
        with self.assertRaises(TypeError):
            Square()

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            Square(None)

    def test_size_type(self):
        # type testing (if the type of size is a string)
        with self.assertRaises(TypeError):
            Square("string")

        # type testing (if the type of size is a list)
        with self.assertRaises(TypeError):
            Square([0, 1, 2])
        with self.assertRaises(TypeError):
            Square([0])
        with self.assertRaises(TypeError):
            Square([])

        # type testing (if the type of size is a float)
        with self.assertRaises(TypeError):
            Square(1.5)

        # type testing (if the type of size is a tuple)
        with self.assertRaises(TypeError):
            Square((0, 1, 2))
        with self.assertRaises(TypeError):
            Square((0, 1))
        with self.assertRaises(TypeError):
            Square(())

    def test_size_value(self):
        # type testing (if the size < 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)


class TestSquareX(unittest.TestCase):
    """ test sqaure: x argument """

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            Square(10, None)

    def test_x_type(self):
        # type testing (if the type of x is a string)
        with self.assertRaises(TypeError):
            Square(10, "x")

        # type testing (if the type of x is a list)
        with self.assertRaises(TypeError):
            Square(10, [0, 1, 2])
        with self.assertRaises(TypeError):
            Square(10, [0])
        with self.assertRaises(TypeError):
            Square(10, [])

        # type testing (if the type of x is a float)
        with self.assertRaises(TypeError):
            Square(10, 1.5)

        # type testing (if the type of x is a tuple)
        with self.assertRaises(TypeError):
            Square(10, (0, 1, 2))
        with self.assertRaises(TypeError):
            Square(10, (0, 1))
        with self.assertRaises(TypeError):
            Square(10, ())

    def test_x_value(self):
        # type testing (if the x < 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -1)


class TestSquareY(unittest.TestCase):
    """ test sqaure: y argument """

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            Square(10, 5, None)

    def test_y_type(self):
        # type testing (if the type of y is a string)
        with self.assertRaises(TypeError):
            Square(10, 5, "x")

        # type testing (if the type of y is a list)
        with self.assertRaises(TypeError):
            Square(10, 5, [0, 1, 2])
        with self.assertRaises(TypeError):
            Square(10, 5, [0])
        with self.assertRaises(TypeError):
            Square(10, 5, [])

        # type testing (if the type of y is a float)
        with self.assertRaises(TypeError):
            Square(10, 5, 1.5)

        # type testing (if the type of y is a tuple)
        with self.assertRaises(TypeError):
            Square(10, 5, (0, 1, 2))
        with self.assertRaises(TypeError):
            Square(10, 5, (0, 1))
        with self.assertRaises(TypeError):
            Square(10, 5, ())

    def test_y_value(self):
        # type testing (if y < 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 5, -1)


class TestSquareAllArgs(unittest.TestCase):
    """ Test Square class Arguments """
    def test_square_base(self):
        self.assertIsInstance(Square(5), Base)

    def test_square_rectangle(self):
        self.assertIsInstance(Square(5), Square)

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_argument(self):
        s_1 = Square(5)
        s_2 = Square(6)
        self.assertEqual(s_1.id, s_2.id - 1)

    def test_two_arguments(self):
        s_1 = Square(5, 6)
        s_2 = Square(4, 3)
        self.assertEqual(s_1.id, s_2.id - 1)

    def test_three_arguments(self):
        s_1 = Square(5, 4, 6)
        s_2 = Square(10, 1, 9)
        self.assertEqual(s_1.id, s_2.id - 1)

    def test_four_arguments(self):
        self.assertEqual(7, Square(5, 2, 2, 7).id)

    def test_more_arguments(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)


class TestSquareArea(unittest.TestCase):
    """ test sqaure: area """

    def test_area_value(self):
        sq_1 = Square(5, 1, 1, 1)
        sq_2 = Square(10, 1, 1, 1)
        sq_3 = Square(100, 1, 1, 1)
        sq_4 = Square(1, 1, 1, 1)

        self.assertEqual(sq_1.area(), 25)
        self.assertEqual(sq_2.area(), 100)
        self.assertEqual(sq_3.area(), 10000)
        self.assertEqual(sq_4.area(), 1)

    def test_area_changing(self):
        sq_1 = Square(5, 1, 1, 1)
        sq_1.size = 10

        sq_2 = Square(10, 1, 1, 1)
        sq_2.size = 11

        sq_3 = Square(100, 1, 1, 1)
        sq_3.size = 12

        sq_4 = Square(1, 1, 1, 1)
        sq_4.size = 13

        self.assertEqual(sq_1.area(), 100)
        self.assertEqual(sq_2.area(), 121)
        self.assertEqual(sq_3.area(), 144)
        self.assertEqual(sq_4.area(), 169)

    def test_area_with_arg(self):
        sq = Square(10, 1, 2, 3)
        with self.assertRaises(TypeError):
            sq.area(10)


class TestSquareStr(unittest.TestCase):
    """ test sqaure: string method """

    def test_str_method_one_arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    def test_str_method_two_arg(self):
        s = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(s.id)
        self.assertEqual(correct, s.__str__())

    def test_str_method_three_args(self):
        s = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_str_method_args(self):
        s = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(s))

    def test_str_method_changing(self):
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))


class TestSquareDisplay(unittest.TestCase):
    """ test sqaure: display method """

    @staticmethod
    def take_stdout(square, method):
        output = io.StringIO()
        sys.stdout = output
        if method == "print":
            print(square)
        else:
            square.display()
        sys.stdout = sys.__stdout__
        return output

    def test_display_size(self):
        s = Square(2, 0, 0, 9)
        capture = TestSquareDisplay.take_stdout(s, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_size_x(self):
        s = Square(3, 1, 0, 18)
        capture = TestSquareDisplay.take_stdout(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_size_y(self):
        s = Square(4, 0, 1, 9)
        capture = TestSquareDisplay.take_stdout(s, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y(self):
        s = Square(2, 3, 2, 1)
        capture = TestSquareDisplay.take_stdout(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)


class TestSquareUpdate(unittest.TestCase):
    """
      Test Square: Update Arguments
      s -> {id, x, y, size}
      format: [Square] (id) x/y - size
    """

    # Test 0
    def test_update_method_zero(self):
        s = Square(10, 1, 6, 2)
        s.update()
        expected = "[Square] (2) 1/6 - 10"
        self.assertEqual(expected, str(s))

    # Test 1
    def test_update_method_id(self):
        s = Square(10, 1, 6, 2)
        s.update(3)
        expected = "[Square] (3) 1/6 - 10"
        self.assertEqual(expected, str(s))

    # Test 2
    def test_update_method_size(self):
        s = Square(10, 1, 6, 2)
        s.update(3, 5)
        expected = "[Square] (3) 1/6 - 5"
        self.assertEqual(expected, str(s))

    # Test 4
    def test_update_method_x(self):
        s = Square(10, 1, 6, 2)
        s.update(3, 5, 2)
        expected = "[Square] (3) 2/6 - 5"
        self.assertEqual(expected, str(s))

    # Test 5
    def test_update_method_y(self):
        s = Square(10, 1, 6, 2)
        s.update(3, 5, 2, 4)
        expected = "[Square] (3) 2/4 - 5"
        self.assertEqual(expected, str(s))

    # update kwargs
    def test_update_kwargs_one(self):
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        s = Square(10, 10, 10, 10)
        s.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))

    def test_update_kwargs_three(self):
        s = Square(10, 10, 10, 10)
        s.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(s))

    def test_update_kwargs_four(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_update_kwargs_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=8)
        self.assertEqual(8, s.width)

    def test_update_kwargs_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=9)
        self.assertEqual(9, s.height)

    def test_update_kwargs_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1)
        s.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(s))

    def test_update_kwargs_invalid_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_kwargs_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_some_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(s))
