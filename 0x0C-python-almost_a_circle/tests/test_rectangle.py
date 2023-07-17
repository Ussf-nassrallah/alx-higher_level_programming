#!/usr/bin/python3

import sys
import io
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


class TestRectangleArea(unittest.TestCase):
    """ test rectangle: area """

    def test_area_value(self):
        r_1 = Rectangle(5, 2, 1, 1, 1)
        r_2 = Rectangle(3, 4, 1, 1, 1)
        r_3 = Rectangle(1, 10, 1, 1, 1)
        r_4 = Rectangle(10, 10, 1, 1, 1)

        self.assertEqual(r_1.area(), 10)
        self.assertEqual(r_2.area(), 12)
        self.assertEqual(r_3.area(), 10)
        self.assertEqual(r_4.area(), 100)

    def test_area_changing(self):
        r_1 = Rectangle(2, 2, 1, 1, 1)
        r_1.width = 3
        r_1.height = 7

        r_2 = Rectangle(10, 8, 1, 1, 1)
        r_2.width = 2
        r_2.height = 2

        r_3 = Rectangle(100, 10, 1, 1, 1)
        r_3.width = 10
        r_3.height = 3

        r_4 = Rectangle(1, 2, 1, 1, 1)
        r_4.width = 15
        r_4.height = 4

        self.assertEqual(r_1.area(), 21)
        self.assertEqual(r_2.area(), 4)
        self.assertEqual(r_3.area(), 30)
        self.assertEqual(r_4.area(), 60)

    def test_area_with_arg(self):
        r = Rectangle(10, 2, 1, 2, 3)
        with self.assertRaises(TypeError):
            r.area(10)


class TestRectangleDict(unittest.TestCase):
    """ Test Rectangle : Dictionary """

    def test_dict_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.to_dictionary(5)

    def test_dict_output(self):
        # Test 1
        r_1 = Rectangle(10, 5, 1, 1)
        dict_1 = r_1.to_dictionary()
        self.assertEqual(dict_1, {
            "id": r_1.id,
            "width": r_1.width,
            "height": r_1.height,
            "x": r_1.x,
            "y": r_1.y
        })
        # Test 2
        r_2 = Rectangle(8, 2, 2, 3, 2)
        dict_2 = r_2.to_dictionary()
        self.assertEqual(dict_2, {
            "id": r_2.id,
            "width": r_2.width,
            "height": r_2.height,
            "x": r_2.x,
            "y": r_2.y
        })
        # Test 3
        r_3 = Rectangle(2, 1, 4, 8, 12)
        dict_3 = r_3.to_dictionary()
        self.assertEqual(dict_3, {
            "id": r_3.id,
            "width": r_3.width,
            "height": r_3.height,
            "x": r_3.x,
            "y": r_3.y
        })


class TestRectangleDisplay(unittest.TestCase):
    """ Test Rectangle : Display Method """


    @staticmethod
    def take_stdout(square, method):
        """
          take_stdout - function thats return :
            The text printed to stdout by calling method on rectangle.
        """
        output = io.StringIO()
        sys.stdout = output
        if method == "print":
            print(square)
        else:
            square.display()
        sys.stdout = sys.__stdout__
        return output

    def test_display_arg(self):
        r = Rectangle(1, 2, 2, 2)
        with self.assertRaises(TypeError):
            r.display(1)

    def test_display_width_height(self):
        # Test 0
        r_0 = Rectangle(1, 1)
        cap_0 = TestRectangleDisplay.take_stdout(r_0, "display")
        self.assertEqual("#\n", cap_0.getvalue())
        # Test 1
        r_1 = Rectangle(2, 2)
        cap_1 = TestRectangleDisplay.take_stdout(r_1, "display")
        self.assertEqual("##\n##\n", cap_1.getvalue())
        # Test 2
        r_2 = Rectangle(3, 3)
        cap_2 = TestRectangleDisplay.take_stdout(r_2, "display")
        self.assertEqual("###\n###\n###\n", cap_2.getvalue())
        # Test 2
        r_3 = Rectangle(4, 2)
        cap_3 = TestRectangleDisplay.take_stdout(r_3, "display")
        self.assertEqual("####\n####\n", cap_3.getvalue())

    def test_display_x(self):
        r = Rectangle(3, 2, 1, 0, 18)
        capture = TestRectangleDisplay.take_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_y(self):
        r = Rectangle(4, 3, 0, 1, 9)
        capture = TestRectangleDisplay.take_stdout(r, "display")
        display = "\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_x_y(self):
        s = Rectangle(2, 3, 3, 2, 1)
        capture = TestRectangleDisplay.take_stdout(s, "display")
        display = "\n\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())


class TestRectangleUpdate(unittest.TestCase):
    """
      Test Rectangle: Update Arguments
      r -> {width, height, x, y, id}
      format: [Rectangle] (id) x/y - width/height
    """

    # Test 0
    def test_update_method_zero(self):
        r = Rectangle(5, 2, 1, 3, 1)
        r.update()
        expected = "[Rectangle] (1) 1/3 - 5/2"
        self.assertEqual(expected, str(r))

    # Test 1
    def test_update_method_id(self):
        r = Rectangle(10, 4, 1, 6, 2)
        r.update(3)
        expected = "[Rectangle] (3) 1/6 - 10/4"
        self.assertEqual(expected, str(r))

    # Test 2
    def test_update_method_width(self):
        r = Rectangle(10, 4, 1, 6, 2)
        r.update(3, 5)
        expected = "[Rectangle] (3) 1/6 - 5/4"
        self.assertEqual(expected, str(r))

    # Test 3
    def test_update_method_height(self):
        r = Rectangle(10, 4, 1, 6, 2)
        r.update(3, 5, 2)
        expected = "[Rectangle] (3) 1/6 - 5/2"
        self.assertEqual(expected, str(r))

    # Test 4
    def test_update_method_x(self):
        r = Rectangle(10, 4, 1, 6, 2)
        r.update(3, 5, 2, 4)
        expected = "[Rectangle] (3) 4/6 - 5/2"
        self.assertEqual(expected, str(r))

    # Test 5
    def test_update_method_y(self):
        r = Rectangle(10, 4, 1, 6, 2)
        r.update(3, 5, 2, 4, 1)
        expected = "[Rectangle] (3) 4/1 - 5/2"
        self.assertEqual(expected, str(r))

    # update kwargs
    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))

