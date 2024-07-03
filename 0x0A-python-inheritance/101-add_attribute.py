#!/usr/bin/python3
"""
module to Write a function that adds a new
attribute to an object if it’s possible
"""


def add_attribute(obj, name, value):
    """method to add"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
