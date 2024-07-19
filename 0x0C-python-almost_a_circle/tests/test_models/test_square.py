#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0  # Resetting the private class attribute

    def test_init(self):
        s = Square(1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

        s = Square(1, 2)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 2)

        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 3)

    def test_size_setter(self):
        s = Square(1)
        with self.assertRaises(TypeError):
            s.size = "2"
        with self.assertRaises(ValueError):
            s.size = -1

    def test_x_y_setter(self):
        s = Square(1)
        with self.assertRaises(TypeError):
            s.x = "2"
        with self.assertRaises(ValueError):
            s.x = -1

        with self.assertRaises(TypeError):
            s.y = "3"
        with self.assertRaises(ValueError):
            s.y = -1

    def test_area(self):
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_display(self):
        s = Square(2, 1, 2)
        output = "\n\n ##\n ##\n"
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
        s = Square(3, 1, 2, 4)
        self.assertEqual(str(s), "[Square] (4) 1/2 - 3")

    def test_update_args(self):
        s = Square(1, 2, 3, 4)
        s.update(10, 20, 30)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 30)
        self.assertEqual(s.y, 30)

    def test_update_kwargs(self):
        s = Square(1, 2, 3, 4)
        s.update(id=10, size=20, x=30, y=40)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 30)
        self.assertEqual(s.y, 40)

    def test_to_dictionary(self):
        s = Square(10, 20, 30, 40)
        expected = {'id': 40, 'size': 10, 'x': 20, 'y': 30}
        self.assertEqual(s.to_dictionary(), expected)

    def test_create(self):
        s = Square.create(id=89, size=1, x=2, y=3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_objects(self):
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as file:
            expected = '[{"id": 1, "size": 1, "x": 0, "y": 0}]'
            self.assertEqual(file.read(), expected)

    def test_load_from_file_not_found(self):
        s = Square.load_from_file()
        self.assertEqual(s, [])

    def test_load_from_file(self):
        s = Square(1)
        Square.save_to_file([s])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].id, 1)
        self.assertEqual(loaded[0].size, 1)

if __name__ == '__main__':
    unittest.main()

