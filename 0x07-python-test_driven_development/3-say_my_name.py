#!/usr/bin/python3
"""module to print say my name"""


def say_my_name(first_name, last_name=""):
    """printing function"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")
    output = print("My name is {} {}".format(first_name, last_name))
    return output
