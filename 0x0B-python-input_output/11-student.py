#!/usr/bin/python3
"""
module to create class student and define it.
"""


class Student():
    """defined class"""
    def __init__(self, first_name, last_name, age):
        """initilizing attribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method to retrieve dict"""
        if (isinstance(attrs, list) and
                all(isinstance(item, str)) for item in attrs):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replace attribute for students"""
        for key, value in json.items():
            setattr(self, key, value)
