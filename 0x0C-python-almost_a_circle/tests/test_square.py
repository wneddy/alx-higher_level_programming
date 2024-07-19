#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0  # Resetting the private class attribute

    def test_init(self):
        s = Square(5, 2, 3, 10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_size_setter(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "10"
        with self.assertRaises(ValueError):
            s.size = -10

    def test_area(self):
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_display(self):
        s = Square(2, 2, 2)
        output = "\n\n  ##\n  ##\n"
        from io import StringIO
        import sys
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            s.display()
            self.assertEqual(out.getvalue(), output)
        finally:
            sys.stdout = saved_stdout

    def test_str(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_update_args(self):
        s = Square(5, 5, 5, 5)
        s.update(89, 10, 20, 30)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 30)

    def test_update_kwargs(self):
        s = Square(5, 5, 5, 5)
        s.update(id=89, size=10, x=20, y=30)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 20)
        self.assertEqual(s.y, 30)

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        s_dict = s.to_dictionary()
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s_dict, expected)

if __name__ == '__main__':
    unittest.main()

