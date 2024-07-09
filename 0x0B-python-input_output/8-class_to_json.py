#!/usr/bin/python3
"""
module to returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """method responsible"""
    return obj.__dict__
