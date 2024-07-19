#!/usr/bin/python3
import unittest
from models.base import Base
import json
import os


class TestBase(unittest.TestCase):
    
    def setUp(self):
        Base._Base__nb_objects = 0  # Resetting the private class attribute
    
    def test_init_with_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)
    
    def test_init_without_id(self):
        b = Base()
        self.assertEqual(b.id, 1)
    
    def test_to_json_string(self):
        dicts = [{"id": 1, "width": 10}, {"id": 2, "height": 20}]
        json_str = Base.to_json_string(dicts)
        self.assertEqual(json_str, json.dumps(dicts))
    
    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")
    
    def test_save_to_file(self):
        class Dummy(Base):
            def to_dictionary(self):
                return {"id": self.id}
        
        d1 = Dummy(1)
        d2 = Dummy(2)
        Dummy.save_to_file([d1, d2])
        
        with open("Dummy.json", "r") as file:
            content = file.read()
        
        self.assertEqual(json.loads(content), [{"id": 1}, {"id": 2}])
    
    def test_save_to_file_none(self):
        class Dummy(Base):
            def to_dictionary(self):
                return {"id": self.id}
        
        Dummy.save_to_file(None)
        
        with open("Dummy.json", "r") as file:
            content = file.read()
        
        self.assertEqual(content, "[]")
    
    def test_from_json_string(self):
        json_str = '[{"id": 1, "width": 10}, {"id": 2, "height": 20}]'
        dicts = Base.from_json_string(json_str)
        self.assertEqual(dicts, [{"id": 1, "width": 10}, {"id": 2, "height": 20}])
    
    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])
    
    def test_create(self):
        class Rectangle(Base):
            def __init__(self, width, height, x=0, y=0, id=None):
                super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
                self.y = y
            
            def update(self, **kwargs):
                for key, value in kwargs.items():
                    setattr(self, key, value)
        
        dictionary = {"id": 5, "width": 2, "height": 3}
        r = Rectangle.create(**dictionary)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
    
    def test_load_from_file(self):
        class Dummy(Base):
            def __init__(self, id=None):
                super().__init__(id)
            
            def to_dictionary(self):
                return {"id": self.id}

            @classmethod
            def create(cls, **dictionary):
                return cls(dictionary["id"])
        
        dummy_list = [Dummy(1), Dummy(2)]
        Dummy.save_to_file(dummy_list)
        
        loaded_list = Dummy.load_from_file()
        self.assertEqual(len(loaded_list), 2)
        self.assertEqual(loaded_list[0].id, 1)
        self.assertEqual(loaded_list[1].id, 2)
    
    def test_load_from_file_not_found(self):
        class Dummy(Base):
            @classmethod
            def create(cls, **dictionary):
                return cls(dictionary["id"])

        if os.path.exists("Dummy.json"):
            os.remove("Dummy.json")

        loaded_list = Dummy.load_from_file()
        self.assertEqual(loaded_list, [])

if __name__ == '__main__':
    unittest.main()

