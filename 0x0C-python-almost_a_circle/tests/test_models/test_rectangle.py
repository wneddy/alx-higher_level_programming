#!/usr/bin/python3
import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0  # Resetting the private class attribute

    def test_init(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 2)

        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 3)

    def test_width_height_setter(self):
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.width = "2"
        with self.assertRaises(ValueError):
            r.width = -1

        with self.assertRaises(TypeError):
            r.height = "3"
        with self.assertRaises(ValueError):
            r.height = -1

    def test_x_y_setter(self):
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.x = "2"
        with self.assertRaises(ValueError):
            r.x = -1

        with self.assertRaises(TypeError):
            r.y = "3"
        with self.assertRaises(ValueError):
            r.y = -1

    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_display(self):
        s = Rectangle(2, 1, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        from io import StringIO
        import sys
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            s.display()
            self.assertEqual(out.getvalue(), expected_output)
        finally:
            sys.stdout = saved_stdout

    def test_str(self):
        r = Rectangle(2, 3, 1, 2, 4)
        self.assertEqual(str(r), "[Rectangle] (4) 1/2 - 2/3")

    def test_update_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30, 40)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 40)

    def test_update_kwargs(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=10, width=20, height=30, x=40, y=50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_to_dictionary(self):
        r = Rectangle(10, 20, 30, 40, 50)
        expected = {'id': 50, 'width': 10, 'height': 20, 'x': 30, 'y': 40}
        self.assertEqual(r.to_dictionary(), expected)

    def test_create(self):
        r = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_objects(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            expected = '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]'
            self.assertEqual(file.read(), expected)

    def test_load_from_file_not_found(self):
        r = Rectangle.load_from_file()
        self.assertEqual(r, [])

    def test_load_from_file(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].id, 1)
        self.assertEqual(loaded[0].width, 1)
        self.assertEqual(loaded[0].height, 2)

if __name__ == '__main__':
    unittest.main()

