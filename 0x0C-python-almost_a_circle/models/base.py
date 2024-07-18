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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string representation of list_objs to file"""
        f = cls.__name__+".json"
        with open(f, "w") as jsonF:
            if list_objs is None:
                jsonF.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_str = cls.to_json_string(list_dicts)
                jsonF.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """return json_string rep"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instance with all attributes"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        f = cls.__name__+".json"
        try:
            with open(f, "r") as fileR:
                contents = fileR.read()
                if contents:
                    list_dicts = cls.from_json_string(contents)
                    insta = [cls.create(**d) for d in list_dicts]
                    return insta
                else:
                    return []
        except FileNotFoundError:
            return []
