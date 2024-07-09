#!/usr/bin/python3
"""
module that appends a string at the end
of a text file (UTF8) and returns the
number of characters added
"""


def append_write(filename="", text=""):
    """method to perform the operation"""
    with open(filename, mode="a", encoding="utf-8") as f:
        output = f.write(text)
        return output
