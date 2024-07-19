#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0  # Resetting the private class attribute

    def test_init(self):
        r = Rectangle(10, 2, 1, 1, 1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_width_setter(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.width = "10"
        with self.assertRaises(ValueError):
            r.width = -10

    def test_height_setter(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.height = "2"
        with self.assertRaises(ValueError):
            r.height = -2

    def test_x_setter(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.x = "1"
        with self.assertRaises(ValueError):
            r.x = -1

    def test_y_setter(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.y = "1"
        with self.assertRaises(ValueError):
            r.y = -1

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_display(self):
        r = Rectangle(2, 3, 2, 2)
        output = "\n\n  ##\n  ##\n  ##\n"
        from io import StringIO
        import sys
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            r.display()
            self.assertEqual(out.getvalue(), output)
        finally:
            sys.stdout = saved_stdout

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        r_dict = r.to_dictionary()
        expected = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r_dict, expected)

if __name__ == '__main__':
    unittest.main()

