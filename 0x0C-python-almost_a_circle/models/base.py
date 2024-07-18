#!/usr/bin/python3
"""
class base module declaration
"""
import json


class Base:
    """base class declared"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialising class attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """converts dict to json(str) format"""
        if list_dictionaries is None or []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
