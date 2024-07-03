#!/usr/bin/python3
"""
module to check if object is an instance of the
specified class.
"""


def is_same_class(obj, a_class):
    """method to return true if obj is an instance"""
    return type(obj) is a_class
